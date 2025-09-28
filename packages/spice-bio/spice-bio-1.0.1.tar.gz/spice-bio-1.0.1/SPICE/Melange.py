from random import random
import numpy as np
from tqdm import tqdm 
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from tqdm import tqdm
import os
import random

from SPICE.Soma import one_hot_encode, OneHotBarcodeDataset, SOMA

# ==== Autoencoder Model ====
class OneHotSeqVAE(nn.Module):
    def __init__(self, input_channels=4, max_len=250, hidden_dim=128, latent_dim=128, num_layers=3, num_heads=8):
        super().__init__()
        self.input_proj = nn.Linear(input_channels, hidden_dim)
        self.pos_embedding = nn.Embedding(max_len, hidden_dim)

        encoder_layer = nn.TransformerEncoderLayer(d_model=hidden_dim, nhead=num_heads, batch_first=True)
        self.encoder = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)

        # VAE-specific layers
        self.fc_mu = nn.Linear(hidden_dim, latent_dim)
        self.fc_logvar = nn.Linear(hidden_dim, latent_dim)

        decoder_layer = nn.TransformerEncoderLayer(d_model=latent_dim, nhead=num_heads, batch_first=True)
        self.decoder = nn.TransformerEncoder(decoder_layer, num_layers=1)

        self.output_proj = nn.Linear(latent_dim, input_channels)

    def reparameterize(self, mu, logvar, noise_scale=1.0):
        std = torch.exp(0.5 * logvar)
        eps = torch.randn_like(std)
        return mu + noise_scale * eps * std

    def forward(self, x, noise_scale=1.0):
        B, C, L = x.shape
        x = x.permute(0, 2, 1)  # [B, L, C]
        x = self.input_proj(x)
        positions = torch.arange(x.size(1), device=x.device).unsqueeze(0).expand(B, -1)
        x = x + self.pos_embedding(positions)

        encoded = self.encoder(x)  # [B, L, hidden_dim]

        # # Compute mean and logvar for each position
        mu = self.fc_mu(encoded)  # [B, L, latent_dim]
        logvar = self.fc_logvar(encoded)  # [B, L, latent_dim]

        # Reparameterization trick
        z = self.reparameterize(mu, logvar, noise_scale=noise_scale)  # [B, L, latent_dim]

        # Decode
        decoded = self.decoder(z)
        logits = self.output_proj(decoded)
        logits = logits.permute(0, 2, 1)  # [B, C, L]

        return logits, mu, logvar

# ==== Load Classifiers ====
def load_classifiers(model_dir, seeds_id, device):
    classifiers = []
    for seed in seeds_id:
        model = SOMA().to(device)
        model.load_state_dict(torch.load(os.path.join(model_dir, f'SOMA_params_seed_{seed}.pth'), map_location=device))
        model.eval()
        classifiers.append(model)
    return classifiers

def kl_loss(mu, logvar):
    return -0.5 * torch.mean(1 + logvar - mu.pow(2) - logvar.exp())

def train(
    df,
    max_len,
    lambda_cls=5.0, 
    batch_size=128,
    epochs=5, 
    device='cuda',
    clf_ids=None,
    mode=None,
    save_path='Melange_params.pth'
):

    seed = 0
    random.seed(seed)
    np.random.seed(seed)    
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
        
    if mode not in ['PSI0to1','PSI1to0','PSI0to0.5','PSI0.5to0','PSI0.5to1','PSI1to0.5']:
        raise ValueError(f"Unknown mode: {mode}, please choose from ['PSI0to1','PSI1to0','PSI0to0.5','PSI0.5to0','PSI0.5to1','PSI1to0.5']")
    
    max_psi = df['psi'].max()
    min_psi = df['psi'].min()
    
    criterion_recon = nn.BCEWithLogitsLoss()
    criterion_cls = nn.MSELoss()
    loss_cls_all = []
    loss_recon_all = []
    
    model = OneHotSeqVAE(input_channels=4, max_len=max_len, hidden_dim=128, num_layers=3, num_heads=8).to(device)
    
    if clf_ids is None:
        raise ValueError("Please provide clf_seeds_id for loading classifiers.")

    classifiers = load_classifiers(model_dir='./', seeds_id=clf_ids, device=device)

    dataset = OneHotBarcodeDataset(df, max_len=max_len)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

    model.train()
    
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)
    
    classifiers = [clf.eval() for clf in classifiers]

    with tqdm(range(epochs), desc="Training", unit="epoch", dynamic_ncols=True) as pbar:
        for epoch in pbar:
            model.train()
            epoch_loss = 0.0
            epoch_recon = 0.0
            epoch_cls = 0.0
            epoch_kl = 0.0

            for step, (inputs, _, psi) in enumerate(dataloader):
                inputs = inputs.to(device)
                psi = psi.to(device)

                optimizer.zero_grad()

                # Forward pass
                outputs, mu, logvar = model(inputs)
                loss_recon = criterion_recon(outputs, inputs)
                kl = kl_loss(mu, logvar)

                # 根据 mode 筛选索引
                if mode in ['PSI0to1', 'PSI0to0.5']:
                    zero_indices = (psi < -3.17).nonzero(as_tuple=True)[0]
                elif mode in ['PSI1to0', 'PSI1to0.5']:
                    zero_indices = (psi > 3.17).nonzero(as_tuple=True)[0]
                else:
                    zero_indices = torch.logical_and(psi > -2, psi < 2).nonzero(as_tuple=True)[0]

                if len(zero_indices) > 0:
                    input_seq = inputs[zero_indices]
                    decoded_seq = torch.sigmoid(outputs[zero_indices])

                    preds_list = []
                    originals_list = []
                    for clf in classifiers:
                        preds_list.append(clf(decoded_seq))
                        originals_list.append(clf(input_seq))

                    preds_mean = torch.stack(preds_list, dim=0).mean(0)
                    originals_mean = torch.stack(originals_list, dim=0).mean(0)
                    
                    if mode in ['PSI0to1', 'PSI0.5to1']:
                        target = max_psi * torch.ones_like(preds_mean)
                    elif mode in ['PSI1to0', 'PSI0.5to0']:
                        target = min_psi * torch.ones_like(preds_mean)
                    else:
                        target = torch.zeros_like(preds_mean)

                    loss_cls = criterion_cls(preds_mean, target)
                else:
                    loss_cls = torch.tensor(0.0, device=device)

                lambda_recon = 1.0
                lambda_kl = 0.005

                loss = lambda_recon * loss_recon + lambda_cls * loss_cls + lambda_kl * kl
                loss.backward()
                optimizer.step()

                loss_recon_all.append(loss_recon.item())
                loss_cls_all.append(loss_cls.item())

                epoch_loss += loss.item()
                epoch_recon += loss_recon.item()
                epoch_cls += loss_cls.item()
                epoch_kl += kl.item()

            avg_loss = epoch_loss / len(dataloader)
            avg_recon = epoch_recon / len(dataloader)
            avg_cls = epoch_cls / len(dataloader)
            avg_kl = epoch_kl / len(dataloader)

            pbar.set_postfix({
                "loss": f"{avg_loss:.4f}",
                "recon": f"{avg_recon:.4f}",
                "cls": f"{avg_cls:.4f}",
                "kl": f"{avg_kl:.4f}",
            })

        pbar.set_postfix({"loss": f"{avg_loss:.4f}", "recon": f"{avg_recon:.4f}", "cls": f"{avg_cls:.4f}"})

    print("Training completed.")
    torch.save(model.state_dict(), save_path)

def evaluate_reconstructions(df, clf_id, max_len=250, device='cuda', params=None):
    """
    Evaluate reconstruction performance across all PSI < 0.1 samples using two classifiers.

    Args:
        df: dataframe containing 'seq' column for k-mer tokenizer.
        model: trained autoencoder model.
        dataloader: DataLoader for evaluation.
        max_len: maximum sequence length.
        device: 'cuda' or 'cpu'.

    Returns:
        mean prediction scores for reconstructed and original sequences from both classifiers.
    """
    
    model = OneHotSeqVAE(input_channels=4, max_len=max_len, hidden_dim=128, num_layers=3, num_heads=8).to(device)
    if params is not None:
        model.load_state_dict(torch.load(params, map_location=device))
    else:
        raise ValueError("Please provide model params for the trained Melange model.")
    
    dataset = OneHotBarcodeDataset(df, max_len=max_len)
    dataloader = DataLoader(dataset, batch_size=1, shuffle=False)
    
    model.eval()
    base_list = ['A', 'T', 'C', 'G']

    # Load barcode classifier
    clf_eval = SOMA().to(device)
    clf_eval.load_state_dict(torch.load(f'SOMA_params_seed_{clf_id}.pth', map_location=device))
    clf_eval.eval()

    preds_barcode = []
    originals_barcode = []

    with torch.no_grad():
        for inputs, seqs, labels in tqdm(dataloader):
            inputs = inputs.to(device)
            labels = labels.to(device)

            for seq in seqs:
                # Encode input
                one_hot = one_hot_encode(seq, max_len=max_len)
                input_tensor = torch.tensor(one_hot).unsqueeze(0).to(device)

                # Model forward
                outputs, _, _ = model(input_tensor)
                probs = torch.sigmoid(outputs).squeeze(0).cpu().numpy()

                # Decode predicted sequence
                pred_seq = ''
                for i in range(probs.shape[1]):
                    base_idx = probs[:, i].argmax()
                    pred_seq += base_list[base_idx]

                input_seq = seq[:max_len]
                pred_seq = pred_seq[:len(input_seq)]

                # Re-encode predicted and original sequences
                pred_onehot = one_hot_encode(pred_seq, max_len=max_len)
                orig_onehot = one_hot_encode(input_seq, max_len=max_len)

                pred_input = torch.tensor(pred_onehot).unsqueeze(0).to(device)
                orig_input = torch.tensor(orig_onehot).unsqueeze(0).to(device)

                # Barcode classifier
                pred_score = clf_eval(pred_input)
                orig_score = clf_eval(orig_input)

                preds_barcode.append(pred_score.squeeze(1).cpu().item())
                originals_barcode.append(orig_score.squeeze(1).cpu().item())

    
    # Compute mean scores
    mean_pred_barcode = np.mean(preds_barcode)
    mean_orig_barcode = np.mean(originals_barcode)

    print(f"Mean prediction of original sequences from the classifier: {mean_orig_barcode:.4f}")
    print(f"Mean prediction of generated sequences from the classifier: {mean_pred_barcode:.4f}")

    return preds_barcode, originals_barcode

# ==== Reconstruction and Visualization ====
def reconstruct_sequence(seq, max_len=250, device='cuda', params=None):
    """
    Reconstruct one sequence and print the original vs reconstructed sequence.

    Args:
        model: trained autoencoder model.
        seq: input sequence string.
        max_len: maximum sequence length.
        device: 'cuda' or 'cpu'.
    """
    model = OneHotSeqVAE(input_channels=4, max_len=max_len, hidden_dim=128, num_layers=3, num_heads=8).to(device)
    if params is not None:
        model.load_state_dict(torch.load(params, map_location=device))
    else:
        raise ValueError("Please provide model params for the trained Melange model.")
    
    model.eval()
    base_list = ['A', 'T', 'C', 'G']

    with torch.no_grad():
        one_hot = one_hot_encode(seq, max_len=max_len)
        input_tensor = torch.tensor(one_hot).unsqueeze(0).to(device)
        outputs, _, _ = model(input_tensor)
        probs = torch.sigmoid(outputs).squeeze(0).cpu().numpy()

        # Decode predicted sequence by argmax
        pred_seq = ''
        for i in range(probs.shape[1]):
            base_idx = probs[:, i].argmax()
            pred_seq += base_list[base_idx]

        # Truncate to match input
        input_seq = seq[:max_len]
        pred_seq = pred_seq[:len(input_seq)]

        # Generate match line
        match_line = ''.join(['✓' if a == b else '✗' for a, b in zip(input_seq, pred_seq)])

        # Print results
        print("Original     :", input_seq)
        print("Reconstructed:", pred_seq)
        print("Match        :", match_line)
        
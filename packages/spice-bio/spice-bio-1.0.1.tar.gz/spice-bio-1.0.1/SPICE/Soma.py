import numpy as np
from tqdm import tqdm
import torch
import random
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import torch.nn.functional as F

class ResNetCNN(nn.Module):
    '''Residual CNN block with multi-scale convolutions'''
    def __init__(self, channels, dropout=0.2):
        super().__init__() 
        
        self.conv1_5 =  nn.Conv1d(channels, channels, kernel_size=5, padding=2)  
        self.conv1_11 = nn.Conv1d(channels, channels, kernel_size=11, padding=5)
        self.conv1_21 = nn.Conv1d(channels, channels, kernel_size=21, padding=10)

        self.batchnorm1 = nn.BatchNorm1d(channels * 3) 
        self.dropout = nn.Dropout(dropout)
        self.conv_merge = nn.Conv1d(channels * 3, channels, kernel_size=1)

        self.conv2 = nn.Conv1d(channels, channels, kernel_size=5, padding=2)
        self.batchnorm2 = nn.BatchNorm1d(channels)

    def forward(self, x):
        residual = x 
        x1 = self.conv1_5(x)
        x2 = self.conv1_11(x)
        x3 = self.conv1_21(x)

        x = torch.cat([x1, x2, x3], dim=1) 

        x = self.dropout(F.relu(self.batchnorm1(x)))
        x = self.conv_merge(x) 
        x = self.dropout(F.relu(self.batchnorm2(self.conv2(x))))
        
        x = x + residual  
        return x

class SequenceCNN(nn.Module):
    '''
    CNN model for processing one-hot encoded DNA sequences
    '''
    def __init__(self):
        super().__init__()
        
        self.dropout = nn.Dropout(0.2)
        
        self.conv1 = nn.Conv1d(in_channels=4, out_channels=128, kernel_size=1, padding='same')
        self.batchnorm1 = nn.BatchNorm1d(128)
    
        self.resnetCNN1 = nn.Sequential(
            ResNetCNN(128),
            ResNetCNN(128),
            ResNetCNN(128),
        )
        
        self.maxpool = nn.MaxPool1d(kernel_size=2)
        
        self.conv2 = nn.Conv1d(in_channels=128, out_channels=64, kernel_size=1, padding='same')
        self.batchnorm2 = nn.BatchNorm1d(64)
        
        self.resnetCNN2 = nn.Sequential(
            ResNetCNN(64),
            ResNetCNN(64),
            ResNetCNN(64),
        )
        
        self.conv3 = nn.Conv1d(in_channels=64, out_channels=16, kernel_size=1, padding='same')
        self.batchnorm3 = nn.BatchNorm1d(16)
        
        self.resnetCNN3 = nn.Sequential(
            ResNetCNN(16),
            ResNetCNN(16),
            ResNetCNN(16),
        )

        self.conv4 = nn.Conv1d(in_channels=128, out_channels=16, kernel_size=1, padding='same')
        self.maxpool8 = nn.MaxPool1d(kernel_size=8)
        
        # Linear layers
        self.fc1 = nn.Linear(in_features=496, out_features=128)
        
    def forward(self, x):
        x = self.dropout(F.relu(self.batchnorm1(self.conv1(x))))
        residual = x
        x_residual = x
        x = self.resnetCNN1(x)
        x = x + residual
        x = self.maxpool(x)
        
        x = self.dropout(F.relu(self.batchnorm2(self.conv2(x))))
        residual = x
        x = self.resnetCNN2(x)
        x = x + residual
        x = self.maxpool(x)
        
        x = self.dropout(F.relu(self.batchnorm3(self.conv3(x))))
        residual = x
        x = self.resnetCNN3(x)
        x = x + residual
        x = self.maxpool(x)
        
        x_residual = self.conv4(x_residual)
        x_residual = self.maxpool8(x_residual)
        
        x = x + x_residual
        
        x = x.view(x.size(0), -1)
        x = self.fc1(x)
        
        return x
    
class SOMA(nn.Module):
    '''
    Full SOMA model combining sequence CNN and final regression layer
    '''
    def __init__(self):
        super().__init__()
        
        self.Barcode_model = SequenceCNN()

        self.fc1 = nn.Linear(in_features=128, out_features=1)
        
        self.dropout = nn.Dropout(0.2)
    
    def forward(self, barcode):
        x = self.Barcode_model(barcode)
        x = self.dropout(F.relu(x))
        x = self.fc1(x)
        
        return x
    
class GexFullyConnected(nn.Module):
    def __init__(self, input_dim):
        super().__init__()

        self.fc1 = nn.Linear(in_features=input_dim, out_features=1024)
        self.fc2 = nn.Linear(in_features=1024, out_features=256)
        self.fc3 = nn.Linear(in_features=256, out_features=128)
        self.BN1 = nn.BatchNorm1d(1024)
        self.BN2 = nn.BatchNorm1d(256) 
        self.dropout = nn.Dropout(0.2)     

    def forward(self, x):
        x = F.relu(self.BN1(self.fc1(x)))
        x = F.relu(self.BN2(self.fc2(x)))
        x = F.relu(self.fc3(x))
        return x
    
class SOMA_with_GEX(nn.Module):
    ''' 
    SOMA model fine-tuned with gene expression data
    '''
    def __init__(self, gex_dim):
        super().__init__()
        
        self.Barcode_model = SequenceCNN()
        self.GX_model = GexFullyConnected(gex_dim)

        self.fc1 = nn.Linear(in_features=128, out_features=64)
        self.bn1 = nn.BatchNorm1d(64)
        self.fc2 = nn.Linear(in_features=64, out_features=1)
        
        self.dropout = nn.Dropout(0.2)
    
    def forward(self, barcode, gx, condition):
        
        z_barcode = self.Barcode_model(barcode)
        
        z_gx = self.GX_model(gx)
        x = z_barcode + z_gx + condition
        x = self.dropout(F.leaky_relu(self.bn1(self.fc1(x))))
        x = self.fc2(x)
        return x

def one_hot_encode(seq, max_len=250):
    '''
    One-hot encode a DNA sequence
    '''
    base_dict = {'A': 0, 'T': 1, 'C': 2, 'G': 3}
    one_hot = np.zeros((4, max_len), dtype=np.float32)
    for i in range(min(len(seq), max_len)):
        if seq[i] in base_dict:
            one_hot[base_dict[seq[i]], i] = 1.0
    return one_hot

class OneHotBarcodeDataset(Dataset):
    '''
    Dataset for one-hot encoded DNA sequences and optional PSI labels
    '''
    def __init__(self, df, max_len=250):
        self.inputs = [one_hot_encode(seq, max_len) for seq in df['seq']]
        self.seqs = df['seq'].values
        if 'psi' in df.columns:
            self.labels = df['psi'].values.astype('float32') 

    def __len__(self):
        return len(self.inputs)

    def __getitem__(self, idx):
        if hasattr(self, 'labels'):
            return torch.tensor(self.inputs[idx]), self.seqs[idx], torch.tensor(self.labels[idx])
        else:
            return torch.tensor(self.inputs[idx]), self.seqs[idx]
        
class OneHotBarcodeGEXDataset(Dataset):
    '''
    Dataset for one-hot encoded DNA sequences with gene expression data and optional PSI labels
    '''
    def __init__(self, df, GX_dict, max_len=250):
        self.samples = []

        for barcode in df.index:

            barcode_array = one_hot_encode(df.loc[barcode, 'seq'], max_len)

            for celltype in df.columns:
                if celltype not in GX_dict:
                    continue
                gx_array = GX_dict[celltype]
                psi_value = df.loc[barcode, celltype]
            
                if not np.isnan(psi_value):
                    self.samples.append((celltype, barcode, barcode_array, gx_array, psi_value))
    
    def __len__(self):
        return len(self.samples)
    
    def __getitem__(self, idx):
        celltype, barcode, barcode_array, gx_array, psi_value = self.samples[idx]
        return celltype, barcode, torch.tensor(barcode_array), torch.tensor(gx_array), torch.tensor(psi_value, dtype=torch.float32)

def train(
    df,
    device,
    max_len=250,
    epochs=100,
    batch_size=256,
    learning_rate=1e-4,
    num_seeds=10,
): 
    '''
    Train the SOMA model
    df: DataFrame with 'seq' and 'psi' columns
    device: 'cuda' or 'cpu'
    max_len: Maximum length of sequences (default 250)
    epochs: Number of training epochs (default 100)
    batch_size: Batch size for training (default 256)
    learning_rate: Learning rate for optimizer (default 1e-4)
    num_seeds: Number of random seeds for training (default 10)
    '''
    assert num_seeds >= 1, "Number of seeds must be at least 1"

    for seed in range(num_seeds):
        random.seed(seed)
        np.random.seed(seed)    
        torch.manual_seed(seed)
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False

        dataset = OneHotBarcodeDataset(df, max_len=max_len)

        train_loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

        model = SOMA().to(device)
        loss_fn = nn.MSELoss()
        optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

        with tqdm(range(epochs), desc="Training", unit="epoch", dynamic_ncols=True) as pbar:
            for epoch in pbar:
                model.train()
                train_loss = 0.0

                for x, _, y in train_loader:
                    x, y = x.to(device), y.to(device)
                    pred = model(x).squeeze(1)
                    loss = loss_fn(pred, y)

                    optimizer.zero_grad()
                    loss.backward()
                    optimizer.step()
                    train_loss += loss.item()

                avg_loss = train_loss / len(train_loader)
                pbar.set_postfix(train_loss=f"{avg_loss:.4f}")

        print(f"Training completed for seed {seed}. Saving model...")
        torch.save(model.state_dict(), f'SOMA_params_seed_{seed}.pth')  # Save the model for each seed
        
def predict(df, device, max_len=250, batch_size=256, params=None):
    '''
    Predict PSI values using the trained SOMA model
    df: DataFrame with 'seq' column
    device: 'cuda' or 'cpu
    max_len: Maximum length of sequences (default 250)
    batch_size: Batch size for prediction (default 256)
    params: Path to the trained model parameters
    '''
    dataset = OneHotBarcodeDataset(df, max_len=max_len, train=False)
    loader = DataLoader(dataset, batch_size=batch_size, shuffle=False)
    
    assert params is not None, "Model parameters must be provided for evaluation."

    model = SOMA().to(device)
    model.load_state_dict(torch.load(params))
    model.eval()
    all_preds = []
    with torch.no_grad():
        for x, _ in tqdm(loader):
            x = x.to(device)
            pred = model(x).squeeze(1)
            all_preds.extend(pred.cpu().numpy())
            
    return np.array(all_preds)
    
def fintune_with_gex(
    df,
    gex_dict,
    device,
    pretrained_params,
    epochs=100,
    learning_rate=1e-4,
    batch_size=256,
):
    '''
    Fine-tune SOMA model with gene expression data
    df: DataFrame with 'seq' and 'psi' columns, indexed by barcode, columns are cell types
    gex_dict: Dictionary mapping cell types to their gene expression numpy arrays
    device: 'cuda' or 'cpu'
    pretrained_model_path: Path to the pre-trained SOMA model parameters
    epochs: Number of fine-tuning epochs (default 100)
    learning_rate: Learning rate for optimizer (default 1e-4)
    batch_size: Batch size for fine-tuning (default 256)
    '''
    gex_dim = list(gex_dict.values())[0].shape[0]
    SOMA_GEX = SOMA_with_GEX(gex_dim)
    SOMA_GEX = SOMA_GEX.to(device)

    SOMA_pretrained = SOMA().to(device)
    SOMA_pretrained.load_state_dict(torch.load(pretrained_params))
    SOMA_pretrained.eval()

    MSELoss = nn.MSELoss()
    optimizer = torch.optim.Adam(SOMA_GEX.parameters(), lr=learning_rate)
    
    train_loader = DataLoader(
        OneHotBarcodeGEXDataset(df, gex_dict), 
        batch_size=batch_size, 
        shuffle=True
    )

    for epoch in range(epochs):
        epoch_loss = 0.0

        with tqdm(train_loader, desc=f"Epoch {epoch+1}/{epochs}", unit="batch", dynamic_ncols=True) as pbar:
            for _, _, barcode, gx, psi in pbar:
                barcode = barcode.to(device).float()
                gx = gx.to(device).float()
                psi = psi.to(device).float()

                optimizer.zero_grad()

                condition = SOMA_pretrained.Barcode_model(barcode).detach()
                psi_pretrain = SOMA_pretrained(barcode).detach()

                psi_residual = SOMA_GEX(barcode, gx, condition)
                psi_loss = MSELoss(psi_residual.squeeze(), psi - psi_pretrain.squeeze())

                psi_loss.backward()
                optimizer.step()

                epoch_loss += psi_loss.item()

                pbar.set_postfix(loss=f"{psi_loss.item():.4f}")

    print("Fine-tuning completed. Saving model...")
    torch.save(SOMA_GEX.state_dict(), "SOMA_with_GEX_params.pth")


def predict_with_gex(
    df, 
    gex_dict, 
    device, 
    pretrained_params,
    pretrained_GEX_params,
    batch_size=256, 
):
    '''
    Predict with fine-tuned SOMA model using gene expression data
    df: DataFrame with 'seq' column, indexed by barcode
    gex_dict: Dictionary mapping cell types to their gene expression numpy arrays
    device: 'cuda' or 'cpu'
    batch_size: Batch size for prediction (default 256)
    params: Path to the fine-tuned model parameters
    '''
    assert pretrained_params is not None, "pretrained_params must be provided for evaluation."
    assert pretrained_GEX_params is not None, "pretrained_GEX_params must be provided for evaluation."

    SOMA_pretrained = SOMA().to(device)
    SOMA_pretrained.load_state_dict(torch.load(pretrained_params))
    SOMA_pretrained.eval()
    
    gex_dim = list(gex_dict.values())[0].shape[0]
    SOMA_GEX = SOMA_with_GEX(gex_dim)
    SOMA_GEX = SOMA_GEX.to(device)
    SOMA_GEX.load_state_dict(torch.load(pretrained_GEX_params))
    SOMA_GEX.eval()

    dataset = OneHotBarcodeGEXDataset(df, gex_dict)
    loader = DataLoader(dataset, batch_size=batch_size, shuffle=False)

    all_preds = []
    with torch.no_grad():
        all_psi = []
        for _, _, barcode, gx, psi in tqdm(loader):
            barcode = barcode.to(device).float()
            gx = gx.to(device).float()
            
            condition = SOMA_pretrained.Barcode_model(barcode).detach()
            psi_residual = SOMA_GEX(barcode, gx, condition).squeeze(1)
            pred = SOMA_pretrained(barcode).squeeze(1) + psi_residual
            all_preds.extend(pred.cpu().numpy())
            all_psi.extend(psi.numpy())
        
        return np.array(all_preds), np.array(all_psi)

    
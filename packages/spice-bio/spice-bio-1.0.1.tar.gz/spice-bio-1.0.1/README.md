# spice-bio
[![PyPI version](https://img.shields.io/pypi/v/spice-bio)](https://pypi.org/project/spice-bio/)
[![Downloads](https://static.pepy.tech/badge/spice-bio)](https://pepy.tech/project/spice-bio)

## Installation
Create a conda environment

```bash
conda create -n spice-env python=3.9
conda activate spice-env
```

Install **spice-bio** via pip:

```bash
pip3 install spice-bio
```
## Examples
Detailed documentation for **SOMA** and **Melange** can be found at folder `examples`.

## SOMA
Here is a simple example of how to use **SOMA** to train a model and predict PSI values:

```python
from SPICE import Soma
import pandas as pd

df_train = pd.read_csv('path/to/your/df_data') # df contains columns 'psi'(ratio) and 'seq'

# train SOMA models, after training, the model parameters will be saved as 'SOMA_params_seed_0.pth', 'SOMA_params_seed_1.pth', etc.
Soma.train(
    df_train,    # pandas DataFrame with columns 'psi' and 'seq'
    device='cuda',    # 'cuda' or 'cpu'
    epochs=1,    # number of training epochs
    batch_size=512,    # batch size
    learning_rate=1e-4,    # learning rate
    num_seeds=10    # number of SOMA models to train with different random initializations
)

df_test = pd.read_csv('path/to/your/df_test_data') # df_test contains column 'seq'

# predict PSI values using a trained SOMA model
pred_psi = Soma.predict(
    df_test,   # pandas DataFrame with column 'seq'
    device='cuda',  # 'cuda' or 'cpu'
    batch_size=512,    # batch size
    params='SOMA_params_seed_0.pth')  # path to the trained SOMA model parameters
```

## Melange
Here is a simple example of how to use **Melange** and **SOMA** to generate sequences with desired PSI values:

```python
from SPICE import Melange
import pandas as pd

df_train = pd.read_csv('path/to/your/df_data') # df contains columns 'psi'(ratio) and 'seq'

Melange.train(
    df_train,    # pandas DataFrame with columns 'psi' and 'seq'
    device='cuda',    # 'cuda' or 'cpu'
    lambda_cls=5.0,   # weight for the classification loss, use to control the trade-off between reconstruction and classification accuracy
    max_len=250,    # maximum sequence length
    epochs=10,      # number of training epochs
    clf_ids=[0,1,2,3,4,5,6,7,8],    # indices of the SOMA models to use as teachers
    mode='PSI1to0',    # choose from {'PSI1to0', 'PSI0to1', 'PSI1to0.5', 'PSI0to0.5', 'PSI0.5to1', 'PSI0.5to0'}
    save_path='Melange_params.pth'    # path to save the trained Melange model parameters
)

df_test = pd.read_csv('path/to/your/df_test_data') # df_test contains column 'seq'

gen_seq_psi_pred, org_seq_psi_pred = Melange.evaluate_reconstructions(
    df_test,    # pandas DataFrame with column 'seq'
    clf_id=9,    # index of the SOMA model to use for evaluation
    device='cuda',    # 'cuda' or 'cpu' 
    max_len=250,    # maximum sequence length
    params='Melange_params.pth'   # path to the trained Melange model parameters
)

# visualize any parent and generated sequence using a trained Melange model
Melange.reconstruct_sequence(
    df_test.iloc[0]['seq'],    # input sequence
    max_len=250,    # maximum sequence length
    device='cuda',    # 'cuda' or 'cpu'
    params='Melange_params.pth'    # path to the trained Melange model parameters
)
```
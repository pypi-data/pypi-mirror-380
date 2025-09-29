import torch
import numpy as np

def to_tensor(X):

    if isinstance(X, np.ndarray):
        return torch.tensor(X, dtype=torch.float32)
    elif isinstance(X, list):
        return torch.tensor(np.array(X), dtype=torch.float32)
    elif isinstance(X, torch.Tensor):
        return X.float()
    else:
        raise TypeError("unsupported input type, expected np.ndarray, list or torch.Tensor")
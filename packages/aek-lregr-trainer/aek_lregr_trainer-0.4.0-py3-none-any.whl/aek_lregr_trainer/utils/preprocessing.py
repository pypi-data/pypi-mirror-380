import torch
import numpy as np
import pandas as pd

def to_tensor(X):

    if isinstance(X, np.ndarray):
        return torch.tensor(X, dtype=torch.float32)
    elif isinstance(X, list):
        return torch.tensor(np.array(X), dtype=torch.float32)
    elif isinstance(X, torch.Tensor):
        return X.float()
    else:
        raise TypeError("unsupported input type, expected np.ndarray, list or torch.Tensor")
    
def load_csv(path, label, as_tensor=True, task="regression"):
    """
    Loads csv file and returns X y.
    With the task parameter you can decide whether to return float or int (for regression, float - for classification, int).
    
    Args:
        path (str): Csv path.
        label (str): Target column name.
        as_tensor (bool): If true it returns PyTorch tensor, if false it returns numpy array.
        task (str): "regression" and "classification".
    
    Returns:
        X, y: (tensor or numpy array)
    """
    df = pd.read_csv(path)
    y = df[label].values
    X = df.drop(columns=[label]).values

    if task == "regression":
        y_dtype = torch.float32
    elif task == "classification":
        y_dtype = torch.long
    else:
        raise ValueError("task must be regression or classification")
    
    if as_tensor:
        X = torch.tensor(X, dtype=torch.float32)
        y = torch.tensor(y, dtype=y_dtype)
    else:
        X = np.array(X, dtype=np.float32)
        y = np.array(y, dtype=np.float32 if task=="regression" else np.int64)
    
    return X, y
import torch
import numpy as np 
from sklearn.metrics import accuracy_score as sk_accuracy
from sklearn.metrics import mean_squared_error as sk_mse
from sklearn.metrics import r2_score as sk_r2


def accuracy_score(y_true, y_pred):

    if isinstance(y_true, torch.Tensor):
        y_true = y_true.cpu().numpy()
    if isinstance(y_pred, torch.Tensor):
        y_pred = y_pred.cpu().numpy()
    return sk_accuracy(y_true, y_pred)

def mean_squared_error(y_true, y_pred):

    if isinstance(y_true, torch.Tensor):
        y_true = y_true.cpu().numpy()
    if isinstance(y_pred, torch.Tensor):
        y_pred = y_pred.cpu().numpy()
    return sk_mse(y_true, y_pred)

def r2_score(y_true, y_pred):

    if isinstance(y_true, torch.Tensor):
        y_true = y_true.cpu().numpy()
    if isinstance(y_pred, torch.Tensor):
        y_pred = y_pred.cpu().numpy()
    return sk_r2(y_true, y_pred)
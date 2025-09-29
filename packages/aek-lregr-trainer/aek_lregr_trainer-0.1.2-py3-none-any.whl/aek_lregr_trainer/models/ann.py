import torch
import torch.nn as nn
import torch.nn.functional as F 

class ANN(nn.Module):
    """
    Basic ANN/DNN model.
    Can be used both classification and regression
    
    Args:
        input_dim (int): Input size.
        hidden_layers (list of int): Each hidden layer neurons.
        output_dim (int): Output size.
        activation (str): Activation function for between hidden layers.(relu, tanh, sigmoid).
    """
    def __init__(self, input_dim, hidden_layers, output_dim, activation="relu"):
        super(ANN, self).__init__()
        self.layers = nn.ModuleList()
        in_dim = input_dim

        for h_dim in hidden_layers:
            self.layers.append(nn.Linear(in_dim, h_dim))
            in_dim = h_dim
        
        self.out = nn.Linear(in_dim, output_dim)

        if activation == "relu":
            self.act_fn = F.relu
        elif activation == "tanh":
            self.act_fn = torch.tanh
        elif activation == "sigmoid":
            self.act_fn = torch.sigmoid
        else:
            raise ValueError("Unsupported activation function")
        
    def forward(self, x):
        for layer in self.layers:
            x = self.act_fn(layer(x))
        x = self.out(x)
        return x
    
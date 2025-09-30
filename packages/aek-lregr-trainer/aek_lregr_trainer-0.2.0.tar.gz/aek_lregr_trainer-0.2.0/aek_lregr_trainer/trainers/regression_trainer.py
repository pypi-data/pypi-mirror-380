import torch
import torch.nn as nn
import torch.optim as optim
from ..models.ann import ANN
from ..utils.preprocessing import to_tensor
from ..utils.metrics import mean_squared_error, r2_score

class RegressionTrainer:

    def __init__(self, input_dim, output_dim=1,
                 hidden_layers=[64, 32], activation="relu",
                 lr=0.001, epochs=10, batch_size=32):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = ANN(input_dim, hidden_layers, output_dim, activation).to(self.device)
        self.epochs = epochs
        self.batch_size = batch_size
        self.criterion = nn.MSELoss()
        self.lr = lr
        self.optimizer = optim.Adam(self.model.parameters(), lr=self.lr)

    def train(self, X, y):
        X = to_tensor(X).to(self.device)
        y = to_tensor(y).to(self.device)

        dataset = torch.utils.data.TensorDataset(X, y)
        loader = torch.utils.data.DataLoader(dataset, batch_size=self.batch_size, shuffle=True)

        self.model.train()
        for epoch in range(self.epochs):
            total_loss = 0
            for xb, yb in loader:
                self.optimizer.zero_grad()
                outputs = self.model(xb)
                loss = self.criterion(outputs, yb)
                loss.backward()
                self.optimizer.step()
                total_loss += loss.item()
            print(f"epoch {epoch+1}/{self.epochs}, loss: {total_loss/len(loader):.4f}")

    def predict(self, X):
        self.model.eval()
        X = to_tensor(X).to(self.device)
        with torch.no_grad():
            outputs = self.model(X)
        return outputs.cpu()
    
    def score(self, X, y, metric="r2"):
        preds = self.predict(X)
        if metric == "r2":
            return r2_score(y, preds)
        elif metric == "mse":
            return mean_squared_error(y, preds)
        else:
            raise ValueError("supported metrics: r2, mse")
        
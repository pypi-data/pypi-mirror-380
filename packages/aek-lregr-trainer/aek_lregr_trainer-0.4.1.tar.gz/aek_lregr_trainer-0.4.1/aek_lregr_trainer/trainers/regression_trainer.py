import torch
import torch.nn as nn
import torch.optim as optim
from ..models.ann import ANN
from sklearn.model_selection import train_test_split
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

    def train(self, X, y, test_size=0.2, random_state=None):
        X = to_tensor(X).to(self.device)
        y = to_tensor(y).to(self.device)

        X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=test_size, random_state=random_state)


        train_dataset = torch.utils.data.TensorDataset(X_train, y_train)
        train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=self.batch_size, shuffle=True)
        
        val_dataset = torch.utils.data.TensorDataset(X_val, y_val)
        val_loader = torch.utils.data.DataLoader(val_dataset, batch_size=self.batch_size, shuffle=False)

        
        for epoch in range(self.epochs):
            self.model.train()
            total_train_loss = 0
            for xb, yb in train_loader:
                self.optimizer.zero_grad()
                outputs = self.model(xb)
                loss = self.criterion(outputs, yb)
                loss.backward()
                self.optimizer.step()
                total_train_loss += loss.item()

            self.model.eval()
            total_val_loss = 0
            with torch.no_grad():
                for xb, yb in val_loader:
                    outputs = self.model(xb)
                    loss = self.criterion(outputs, yb)
                    total_val_loss += loss.item()
            self.model.train()
            print(f"epoch {epoch+1}/{self.epochs} | train loss: {total_train_loss/len(train_loader):.4f} | val loss: {total_val_loss/len(val_loader):.4f}")


    def train2(self, csv_path, label_column):
        from ..utils.preprocessing import load_csv

        X, y = load_csv(csv_path, label=label_column, as_tensor=True, task="regression")
        self.train(X, y)

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
        
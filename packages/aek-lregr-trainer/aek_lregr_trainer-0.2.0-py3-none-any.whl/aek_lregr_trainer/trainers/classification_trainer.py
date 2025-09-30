import torch
import torch.nn as nn
import torch.optim as optim
from ..models.ann import ANN
from ..utils.preprocessing import to_tensor
from ..utils.metrics import accuracy_score

class ClassificationTrainer:

    def __init__(self, input_dim, output_dim,
                  hidden_layers=[64,32], activation="relu",
                    lr=0.001, epochs=10, batch_size=32):
        
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = ANN(input_dim, hidden_layers, output_dim, activation).to(self.device)
        self.epochs = epochs
        self.batch_size = batch_size
        self.lr = lr
        self.criterion = nn.CrossEntropyLoss()
        self.optimizer = optim.Adam(self.model.parameters(), lr=self.lr)

    
    def train(self, X, y):
        X = to_tensor(X).to(self.device)
        y = torch.tensor(y, dtype=torch.long).to(self.device)

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
    
    def train2(self, csv_path, label_column):
        from ..utils.preprocessing import load_csv

        X, y = load_csv(csv_path, label_column, as_tensor=True, task="classification")
        self.train(X, y)

    def predict(self, X):
        self.model.eval()
        X = to_tensor(X).to(self.device)
        with torch.no_grad():
            outputs = self.model(X)
            preds = torch.argmax(outputs, dim=1)
        return preds.cpu()
    
    def score(self, X, y):
        preds = self.predict(X)
        return accuracy_score(y, preds)
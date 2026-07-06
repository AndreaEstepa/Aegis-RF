import torch
import numpy as np
from processors import SignalProcessor
from models import AnomalyDetector

processor = SignalProcessor()
INPUT_SIZE = 33 * 10
model = AnomalyDetector(INPUT_SIZE)
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
criterion = torch.nn.MSELoss()

#training function
def train_model(data_loader, epochs=10):
    model.train()
    for epoch in range(epochs):
        for batch in data_loader:
            optimizer.zero_grad()
            output = model(batch)
            loss = criterion(output, batch.view(batch.size(0), -1))
            loss.backward()
            optimizer.step()
        print(f"Epoch {epoch} completada. Loss: {loss.item():.4f}")

# detection function
def detect_anomaly(new_signal, threshold=0.05):
    model.eval()
    spec = processor.normalize(processor.get_spectrogram(new_signal))
    spec_tensor = torch.FloatTensor(spec.flatten()).unsqueeze(0)
    
    with torch.no_grad():
        reconstruction = model(spec_tensor)
        error = torch.mean((spec_tensor - reconstruction)**2)
    
    return error.item() > threshold, error.item()

print("Sistema Aegis-RF cargado correctamente.")

def train_model(model, dataloader, epochs=50):
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    criterion = torch.nn.MSELoss()
    
    model.train()
    for epoch in range(epochs):
        total_loss = 0
        for batch in dataloader:
            optimizer.zero_grad()
            output = model(batch)
            loss = criterion(output, batch.view(batch.size(0), -1))
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        if epoch % 10 == 0:
            print(f"Epoch {epoch} | Loss: {total_loss/len(dataloader):.6f}")
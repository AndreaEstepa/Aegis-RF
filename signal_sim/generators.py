import numpy as np
from scipy import signal

class SignalProcessor:
    def __init__(self, nperseg=64, noverlap=32):
            self.nperseg = nperseg
            self.noverlap = noverlap

    def get_spectrogram(self, iq_signal):
        f, t, Zxx = signal.stft(iq_signal, nperseg=self.nperseg, noverlap=self.noverlap)
        spectrogram = np.abs(Zxx)
        return spectrogram

    def normalize(self, data):
        return (data - np.min(data)) / (np.max(data) - np.min(data) + 1e-9)



        import torch
import torch.nn as nn

class AnomalyDetector(nn.Module):
    def __init__(self, input_dim):
        super(AnomalyDetector, self).__init__()
        #encoder
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 32)
        )
        #decoder
        self.decoder = nn.Sequential(
            nn.Linear(32, 128),
            nn.ReLU(),
            nn.Linear(128, input_dim),
            nn.Sigmoid()
        )

    def forward(self, x):
        #flatten the input for the linear layers
        x = x.view(x.size(0), -1) 
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded

    def compute_anomaly_score(self, original, reconstructed):
        #reconstruction erro,r anomly score
        return torch.mean((original.view(original.size(0), -1) - reconstructed)**2, dim=1)
import numpy as np
from scipy import signal

class SignalProcessor:
    def __init__(self, nperseg=64):
        self.nperseg = nperseg

    def get_spectrogram(self, iq_signal):
        f, t, Zxx = signal.stft(iq_signal, nperseg=self.nperseg)
        return np.abs(Zxx)

    def normalize(self, data):
        #normalization 4 deep learning
        return (data - np.min(data)) / (np.max(data) - np.min(data) + 1e-9)
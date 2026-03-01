import numpy as np

def generate_time(fs, duration):
    N = int(fs * duration)
    t = np.arange(N) / fs
    return t

def bpsk_modulation(fs, fc, duration, symbol_rate):
    t = generate_time(fs, duration)
    N = len(t)
    
    symbols = np.random.randint(0, 2, int(duration * symbol_rate))
    symbol_samples = int(fs / symbol_rate)
    
    phase = np.repeat(symbols * np.pi, symbol_samples)
    phase = phase[:N]
    
    signal = np.exp(1j * (2*np.pi*fc*t + phase))
    
    return signal.astype(np.complex64)

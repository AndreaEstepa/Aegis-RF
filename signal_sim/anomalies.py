def broadband_jammer(signal, fs, start_time, duration, power_factor=5):
    N = len(signal)
    t = np.arange(N) / fs
    
    mask = (t > start_time) & (t < start_time + duration)
    
    jammer = power_factor * (
        np.random.randn(N) + 1j*np.random.randn(N)
    )
    
    signal[mask] += jammer[mask]
    
    return signal

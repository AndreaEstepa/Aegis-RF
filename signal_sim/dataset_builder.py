import numpy as np
import os
from generators import SignalGenerator

def build_dataset(num_samples=1000, output_dir="data"):
    os.makedirs(f"{output_dir}/train", exist_ok=True)
    gen = SignalGenerator()
    
    print(f"Generando {num_samples} muestras...")
    
    for i in range(num_samples):
        #clean sig
        signal = gen.create_base_signal(duration=0.1, fc=1000)
        #add noise and channel effects
        signal = gen.apply_channel_effects(snr_db=np.random.uniform(10, 20))
        np.save(f"{output_dir}/train/sample_{i}.npy", signal)
        
    print("Dataset generado exitosamente.")

if __name__ == "__main__":
    build_dataset()
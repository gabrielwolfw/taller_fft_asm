from math import cos, pi
import numpy as np

def modulate(signal, t_duration, f_c=5000, f_m=10, A_c=50, A_m=40, sample_rate=20000):
    # Crear vector de tiempo
    t = np.linspace(0, t_duration, len(signal))
    
    # Calcular la envolvente y la portadora
    envelope = A_c + A_m * np.cos(2 * pi * f_m * t)
    carrier = np.cos(2 * pi * f_c * t)
    
    # Modular la señal
    modulated_signal = envelope * carrier
    
    # Centrar y escalar la señal para el rango del DAC (0-255) (para despues implementar en ESP32)
    dac_offset = 128
    modulated_signal = dac_offset + modulated_signal
    
    # Clipear valores fuera de rango
    modulated_signal = np.clip(modulated_signal, 0, 255)
    
    # Convertir a enteros
    return modulated_signal.astype(int)
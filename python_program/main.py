from modulacion import modulate
from demodulacion import demodulate
import numpy as np
from math import pi
import matplotlib.pyplot as plt

def plot_modulated_signal(original_signal, modulated_signal, demodulated_signal, t_duration, sample_rate=20000):
    """
    Grafica la señal original y la señal modulada.
    
    Args:
        original_signal: Array con la señal original
        modulated_signal: Array con la señal modulada
        t_duration: Duración total de la señal en segundos
        sample_rate: Frecuencia de muestreo en Hz
    """
    # Crear vector de tiempo
    t = np.linspace(0, t_duration, len(original_signal))
    
    # Crear la figura con dos subplots
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8), sharex=True)
    
    # Graficar señal original
    ax1.plot(t, original_signal)
    ax1.set_title('Señal Original')
    ax1.set_xlabel('Tiempo (s)')
    ax1.set_ylabel('Amplitud')
    ax1.grid(True)
    
    # Graficar señal modulada
    ax2.plot(t, modulated_signal)
    ax2.set_title('Señal Modulada')
    ax2.set_xlabel('Tiempo (s)')
    ax2.set_ylabel('Amplitud')
    ax2.grid(True)

    # graficar la señal demodulada
    ax3.plot(t, demodulated_signal)
    ax3.set_title('Señal Demodulada')
    ax3.set_xlabel('Tiempo (s)')
    ax3.set_ylabel('Amplitud')
    ax3.grid(True)

    # Ajustar espaciado entre subplots
    plt.tight_layout()
    
    # Mostrar la gráfica
    plt.show()

def main():
    # Crear una señal de ejemplo (1 segundo de duración)
    duration = 1.0  # segundos
    sample_rate = 20000
    f_c = 7000  # Frecuencia de la portadora
    f_m = 200   # Frecuencia de la moduladora
    A_c = 50    # Amplitud de la portadora
    A_m = 40    # Amplitud de la moduladora
    num_samples = int(duration * sample_rate)
    
    # Crear una señal simple (por ejemplo, un seno)
    t = np.linspace(0, duration, num_samples)
    input_signal = np.sin(2 * pi * 200 * t)  # Señal de 400 Hz
    
    # Modular la señal
    modulated = modulate(input_signal, duration, f_c, f_m, A_c, A_m, sample_rate)

    demodulated = demodulate(modulated)

    plot_modulated_signal(input_signal, modulated, demodulated, duration, sample_rate)

if __name__ == "__main__":
    main()
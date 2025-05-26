from machine import DAC, Pin
from math import cos, pi
import time

# DAC en GPIO25
dac = DAC(Pin(25))

# Frecuencias (en Hz)
f_c = 5000   # Portadora
f_m = 50     # Moduladora (usa un valor bajo para ver la envolvente)

# Amplitudes
A_c = 50     # Amplitud de la portadora
A_m = 40     # Amplitud de la moduladora (≤ A_c para evitar sobre-modulación)

# Muestras por segundo
sample_rate = 20000  # 20 kHz (debe ser mayor que 2*f_c por Nyquist)
dt = 1 / sample_rate

# Centro del DAC (para que la señal esté entre 0–255)
dac_offset = 128

T_m = 1 / f_m  # Periodo de la moduladora

# Generador de señal AM en tiempo real
t = 0
while True:
    # Señal AM: envolvente modulando la portadora
    env = A_c + A_m * cos(2 * pi * f_m * t)  # envolvente
    carrier = cos(2 * pi * f_c * t)          # portadora
    val = int(dac_offset + env * carrier)

    # Clipping al rango del DAC
    val = max(0, min(255, val))

    dac.write(val)
    print(val)
    t += dt

    if t >= T_m:
        t = 0
    #time.sleep_us(int(dt * 1_000_000))
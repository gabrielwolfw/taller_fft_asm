import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque

# CONFIGURA TU PUERTO SERIAL Y BAUDRATE
PORT = 'COM3'  # Cambia esto según tu sistema ('/dev/ttyUSB0' en Linux, COMx en Windows)
BAUDRATE = 115200
BUFFER_SIZE = 1000  # Cantidad de muestras visibles en pantalla (BUFFER_SIZE = samples * frecuency * T segundos que quiere mostrar)

# Conectar al puerto serie
ser = serial.Serial(PORT, BAUDRATE, timeout=1)

# Inicializar buffer
data = deque([0] * BUFFER_SIZE, maxlen=BUFFER_SIZE)

# Inicializar figura de Matplotlib
fig, ax = plt.subplots()
line, = ax.plot(data)
ax.set_ylim(0, 255)
ax.set_title("Señal demodulada desde receptor AM")
ax.set_xlabel("Tiempo (muestras)")
ax.set_ylabel("Valor DAC (0–255)")
ax.grid(True)

# Función de actualización para animación
def update(frame):
    while ser.in_waiting:
        try:
            line_raw = ser.readline().decode().strip()
            if line_raw:
                value = int(line_raw)
                data.append(value)
        except ValueError:
            continue
    line.set_ydata(data)
    return line,

# Animación en vivo
ani = animation.FuncAnimation(fig, update, interval=10, blit=True)

# Mostrar gráfico
plt.tight_layout()
plt.show()

# Cierra el puerto al cerrar la ventana
ser.close()
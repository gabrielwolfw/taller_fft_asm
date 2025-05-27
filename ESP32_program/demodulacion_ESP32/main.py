from machine import ADC, DAC, Pin
import time

# Configurar ADC
adc = ADC(Pin(34))  # Asegúrate de usar un pin válido
adc.atten(ADC.ATTN_11DB)  # Rango completo (0-3.6V)
adc.width(ADC.WIDTH_9BIT)  # Resolución: 0-511

# Configurar DAC
dac = DAC(Pin(25))

alpha = 0.05  # Cuanto más pequeño, más filtrado (más lento pero más limpio)
filtered_value = 0


def low_pass_filter(value):
    global filtered_value
    filtered_value = alpha * value + (1 - alpha) * filtered_value
    return filtered_value

# Loop principal
while True:
    raw = adc.read()
    
    # Simular rectificación (valor absoluto con respecto al centro)
    rectified = abs(raw - 256)

    # Filtro pasa bajas (detector de envolvente)
    demodulated = low_pass_filter(rectified)
    
    print(int(demodulated))  # Aquí obtienes la envolvente de la señal (la señal original moduladora)
    dac.write(int(demodulated))
    
    time.sleep_us(int((1/20000) * 1_000_000))
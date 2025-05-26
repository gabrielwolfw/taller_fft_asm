from machine import ADC, DAC, Pin
import time

def low_pass_filter(value, alpha, filtered_value):
    return alpha * value + (1 - alpha) * filtered_value

def demodular_buffer(buffer, alpha=0.05, dac_offset=0, dac_pin=25):

    demodulated_buffer = []
    filtered_value = 0
    dac = DAC(Pin(dac_pin))

    for raw in buffer:
        rectified = abs(raw - 256)  
        filtered_value = low_pass_filter(rectified, alpha, filtered_value)
        demodulated = int(filtered_value + dac_offset)
        if demodulated < 0:
            demodulated = 0
        elif demodulated > 255:
            demodulated = 255
        demodulated_buffer.append(demodulated)
        if dac:
            dac.write(demodulated)
    return demodulated_buffer

def adquirir_buffer(adc_pin=34, duracion_segundos=10, frecuencia_muestreo=20000):
    adc = ADC(Pin(adc_pin))
    adc.atten(ADC.ATTN_11DB)
    adc.width(ADC.WIDTH_9BIT)  # 0-511

    buffer = []
    periodo = 1 / frecuencia_muestreo
    start_time = time.ticks_ms()
    while time.ticks_diff(time.ticks_ms(), start_time) < duracion_segundos * 1000:
        buffer.append(adc.read())
        time.sleep(periodo)
    return buffer

# Lo que se deberia de pegar en main
# buffer = adquirir_buffer()
# resultado = demodular_buffer(buffer, alpha=0.05, dac_offset=128)
# print(resultado)
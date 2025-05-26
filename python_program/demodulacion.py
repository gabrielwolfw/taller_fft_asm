def low_pass_filter(value, alpha, filtered_value):
        filtered_value = alpha * value + (1 - alpha) * filtered_value
        return filtered_value

def demodulate(buffer):
    alpha = 0.10  
    filtered_value = 0
    demodulated = []

    for raw in buffer:
        rectified = abs(raw - 128)
        # Filtro pasa bajas (detector de envolvente)
        filtered_value = low_pass_filter(rectified, alpha, filtered_value) 
        demodulated.append(filtered_value)
        
    return demodulated
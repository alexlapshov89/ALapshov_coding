import numpy as np
def half_range_predict(number:int=1)->int:
    # Алгоритм двукратного деления диапазона поиска
    lim_high = 101  # Верхний порог диапазона
    lim_low = 1     # Нижний порог диапазона
    count = 0
    while True:
        count += 1
        predict_number = int((lim_low + lim_high)/2)
        if predict_number>number:
            lim_high = predict_number
        elif predict_number<number:
            lim_low = predict_number
        elif predict_number==number:
            break
    return count

print(f'Количество попыток: {half_range_predict()}')
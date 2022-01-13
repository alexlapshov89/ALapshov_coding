# Игра "Угадай число"
import numpy as np
number = np.random.randint(1,101)   # Загаданное число
count = 0
while True:
    count += 1
    predict_number = int(input('Введите число:'))   # Попытка угадать
    if predict_number<number:
        print ('Число должно быть больше')
    elif predict_number>number:
        print ('Число должно быть меньше')
    else:
        print ('Вы угадали число ({}) за {} попыток'.format(number,count))
        break    
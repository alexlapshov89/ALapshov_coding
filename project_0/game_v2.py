import numpy as np
def random_predict(number:int=1)->int:
# Алгоритм случайного угадывания числа 
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1,101)
        if predict_number==number:
            break
    return count

#RUN
num = np.random.randint(1,101)
print(f'Число попыток: {random_predict(num)}')
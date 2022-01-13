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
def score_game(func_predict) -> int:
    """
    Возвращает среднее количество попыток на 1000 измерений для
    алгоритма func_predict. В каждом измерении для угадывания генерируется
    число от 1 до 100

    Args:
        func_predict(): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для вопроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(func_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток
    namefunc = str(func_predict.__name__)
    
    return score,namefunc

# RUN
if __name__ == "__main__":
    value,name_algo = score_game(random_predict)
    print(f'Алгоритм "{name_algo}" угадывает число в среднем за: {value} попыток')
# Game "Get number"
import numpy as np
number = np.random.randint(1,101)
count = 0
while True:
    count += 1
    predict_number = int(input('Input number:'))
    if predict_number<number:
        print ('The number must be greater')
    elif predict_number>number:
        print ('The number must be less')
    else:
        print ('You guessed the number ({}) for {} attempts'.format(number,count))
        break    
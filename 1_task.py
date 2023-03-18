"""
На столе лежат n монеток. Некоторые из них лежат вверх решкой,
а некоторые – гербом. Определите минимальное число монеток,
которые нужно перевернуть, чтобы все монетки были повернуты вверх
одной и той же стороной. Выведите минимальное количество монет,
которые нужно перевернуть
"""

import random

count_zero = 0
count_one = 0
count_coins = input('Введите количесвто монеток: ')
try:
    count_coins = int(count_coins)
except ValueError:
    print('Ввели не число')
else:
    for i in range(int(count_coins)):
        coin_side = random.randint(0, 1)
        if coin_side == 0:
            count_zero += 1
        else:
            count_one += 1
    print(count_zero, count_one)
    if count_zero > count_one:
        print(f'Необходимо перевернуть {count_one} монеток')
    else:
        print(f'Необходимо перевернуть {count_zero} монеток')

"""
Требуется вывести все целые степени двойки (т.е. числа вида 2k),
не превосходящие числа N.
"""

number = input('Введите конечное число: ')
i = 0
try:
    number = int(number)
except ValueError:
    print('Было введено не число')
else:
    while 2 ** i <= number:
        print(f'2 в степени {i} равняеться {2 ** i}')
        i += 1

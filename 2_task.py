"""
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
Петя помогает Кате по математике. Он задумывает два натуральных
числа X и Y (X,Y≤1000), а Катя должна их отгадать.
Для этого Петя делает две подсказки. Он называет сумму этих чисел
S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
"""


summ_of_two_numbers = input('Введите сумму двух искомых чисел: ')
product_of_two_numbers = input('Введите произведение двух искомых чисел: ')
first_number = None
second_number = None
try:
    summ_of_two_numbers = int(summ_of_two_numbers)
    product_of_two_numbers = int(product_of_two_numbers)
except ValueError:
    print('Одно из указанных значений не являеться числом')
else:
    for i in range(int(summ_of_two_numbers)):
        for j in range(int(product_of_two_numbers)):
            if summ_of_two_numbers == i+j and product_of_two_numbers == i*j:
                first_number = i
                second_number = j
if first_number != None and second_number != None:
    print(f'Загаданные числа {first_number} и {second_number}')
else:
    print('Были указаны неверные значения суммы и произведения чисел')




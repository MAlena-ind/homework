"""
1)	Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division_numbers(num_1, num_2):
    """ 'Деление первого аргумента на второй. """
    try:
        division = round(num_1 / num_2, 2)
        print(division)
        return division
    except ZeroDivisionError:
        print('Второе число - 0. Делить на ноль нельзя.')


num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
result = division_numbers(num_1, num_2)
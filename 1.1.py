"""
1.	Поработайте с переменными, с
оздайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные,
выведите на экран.
"""


# вывод на экран переменнтой класса int
var_1 = 35
print(var_1)
print(type(var_1))


# запрос у пользователя чисел и строк, сохранение в переменные и вывод на экран
name = input('Введите Ваше имя: ')
age = int(input('Сколько Вам лет?:  '))

print('Пациент: {}.\nВозраст (лет): {}.'.format(name, age))
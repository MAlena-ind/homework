# 4)	Программа принимает действительное положительное число x и целое отрицательное число y.
#     Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
#     При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.


# # Первый — возведение в степень с помощью оператора**
def operator_2_stars(x, y):
    result = round((1/(x**abs(y))), 6)
    return result

# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
def make_for(x, y):
    """определяем детиль с помощью цикла"""
    divider = x
    for i in range(1, abs(y)):
        i += 1
        divider = divider * x
    result = round(1 / divider, 6)
    return result




x = float(input('Введите любое положительное число: '))
y = int(input('Введите целое отрицательное число: '))
while y > -1:
    y = int(input('Введите целое отрицательное число еще раз: '))

result_1 = operator_2_stars(x, y)
print(result_1)

result_2 = make_for(x, y)
print(result_2)
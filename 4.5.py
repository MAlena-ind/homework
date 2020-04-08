# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

def my_func (num1, num2):
    return num1 * num2

my_list = [number for number in range(100, 1001) if number % 2 == 0]
print(my_list)
print(reduce(my_func, my_list))
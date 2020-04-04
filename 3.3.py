 # 3)	Реализовать функцию my_func(),
# которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(num_1, num_2, num_3):
    numbers=[num_1, num_2, num_3]
    numbers=sorted(numbers)
    del numbers[0]
    sum_numb = sum(numbers)
    return sum_numb


num_1=int(input('Введите число 1: '))
num_2=int(input('Введите число 2: '))
num_3=int(input('Введите число 3: '))
result=my_func(num_1, num_2, num_3)
print(result)
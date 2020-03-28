"""
ПРОБА! Не РАБОТАЕТ!
4.	Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
number = input('Введите число из нескольких знаков: ')
i = 0

while i < (len(number) - 1):
	if int(number[i]) >= int(number[i + 1]):
		max_number = int(number[i])
	else:
		max_numb = int(number[i+1])
		i += 1
print('Самая большая цифра: ', max_numb)
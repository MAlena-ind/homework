# 5)	Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.




def input_sum_number(file):
    numbers = input('Введите числа, разделяя их пробелами: ')
    file.write(numbers) # запишем числа в файл, строкой с пробелами
    numbers = numbers.split() # делаем список из строк
    numbers_list = [] # переводим строки в инты
    for i in range(len(numbers)):
        number = int(numbers[i])
        numbers_list.append(number)
    result = sum(numbers_list)
    return result


with open('my_file_2.txt', 'w', encoding='utf-8') as f:
    print(input_sum_number(f))
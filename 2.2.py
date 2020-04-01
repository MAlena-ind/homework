"""
2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

my_list = []
len_my_list = int(input('Сколько элементов будет содержать Ваш список?: '))

try_count = 0

while True:
    element = int(input('Добавьте число в список. Еще {}: '.format(len_my_list - try_count)))
    my_list.append(element)
    try_count += 1
    if len(my_list) == len_my_list:
        break

exchange_list = my_list[:]

final_list = []
end_element = None
if len(exchange_list) % 2 != 0:
    end_element = exchange_list.pop()

while exchange_list:
    a = exchange_list[1]
    b = exchange_list[0]
    final_list.append(a)
    final_list.append(b)
    del exchange_list[:2]

if end_element:
    final_list.append(end_element)

print('Ваш список:', my_list)
print('Список по заданию:', final_list)
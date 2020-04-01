# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]
# вариант решения 1, через условый оператор if
my_list_copy = my_list.copy()

user_number = int(input('Введите число: '))

if user_number in my_list:
    place_number = my_list.index(user_number)
    my_list.insert(place_number + 1, user_number)
elif my_list[0] > user_number > my_list_copy.pop():
    for i in range(len(my_list)):
        if my_list[i+1] < user_number < my_list[i]:
            my_list.insert(i+1, user_number)
else:
    my_list.insert(0, user_number) if user_number > my_list[0] else my_list.append(user_number)
print(my_list)




# вариант решения 2, через функцию sored
user_number = int(input('Введите число: '))
my_list.append(user_number)
print(sorted(my_list, reverse=True))
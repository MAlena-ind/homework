"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

# version_list
seasons = ['Зима', 'Весна', 'Лето', 'Осень']

while True:
    user_month = int(input('Введите порядковый номер месяца: '))
    if user_month < 1 or user_month > 12:
        print('Месяцев в году 12, пробуйте еще раз')
        continue
    elif user_month == 12 or 1 <= user_month < 3:
        i = 0
        break
    elif 2 < user_month < 6:
        i = 1
        break
    elif 5 < user_month < 9:
        i = 2
        break
    else:
        i = 3
        break

print('Время года: ', seasons[i])



# version_dict 

seasons = {
    1: 'Зима',
    2: 'Зима',
    12: 'Зима',
    3: 'Весна',
    4: 'Весна',
    5: 'Весна',
    6: 'Лето',
    7: 'Лето',
    8: 'Лето',
    9: 'Осень',
    10: 'Осень',
    11: 'Осень'
}

while True:
    user_month = int(input('Введите порядковый номер месяца: '))
    if user_month < 1 or user_month > 12:
        print('Месяцев в году 12, пробуйте еще раз')
        continue
    else:
        break

print('Время года: ', seasons[user_month])
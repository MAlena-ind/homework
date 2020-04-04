# 2)	Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.


def information_user(**kwargs):
    """ Реализация вывода данных о пользователе одной сторокой"""
    print('Имя: ', kwargs.get('u_name'), ', Фамилия: ', kwargs.get('u_surname'),
          ', Год рождения: ', kwargs.get('u_y_b'), ', Эл.адрес: ', kwargs.get('u_mail'),
    ', Телефон: ', kwargs.get('u_tel'))


name = input('Ваше имя: ')
surname = input('Ваша фамилия: ')
year_birth = input('Год рождения: ')
city = input('Город проживания: ')
e_mail = input('Электронный адрес: ')
telephone = input('Номер телефона: ')

information_user(u_name=name, u_surname=surname, u_y_b=year_birth, u_city=city, u_mail=e_mail, u_tel=telephone)
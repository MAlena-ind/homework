# 3)    Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32






#функция для определения списка сотрудников с окладом менее 20 000
def salary_less_20000(file):
    result = [] #список сотрдуников с окладом меньше 20 000 руб.
    while True: #пока есть строки
        line = file.readline() #читаем строки, выполнять по 1й строке
        if line:
            line_list = line.split()
            salary = float(line_list[1])
            if salary < 20000:
                result.append(line_list[0])
        else:
            return result

# функция для определения среднего оклада сотрудников фирмы:
def medium_salary(file):
    sum_salary = [] #сумма всех окладов сотрудников
    while True:
        line = file.readline()
        if line:
            line_list = line.split()
            salary = float(line_list[1])
            sum_salary.append(salary) # добавляем второе значение списка в флотовом формате в список всех окладов

        else:
            result = ('Средний оклад в компании: ', sum(sum_salary) / len(sum_salary))
            return result



with open('my_file_2.txt', 'r', encoding='utf-8') as f:
    print(salary_less_20000(f))

with open('my_file_2.txt', 'r', encoding='utf-8') as f:
    print(medium_salary(f))
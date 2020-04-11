# 7)	Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать
# данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
#     Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.




import json

def profit(company):
    profit = int(company[2]) - int(company[3])
    return profit



with open('my_file_2.txt', 'r', encoding='utf-8') as f:
    profit_companies = 0 # Отрицательные прибыли не прибавляем
    count_profit_companies = 0 #Число компаний с прибылью
    profit_comp_dict = {} #Словарь: компания с прибылью: размер прибыли
    average_profit_companies_dict = {} #Словарь вида: средняя прибыль: значение
    not_profit_companies_dict = {} #Словарь: компания с отрицательной прибылью: размер убытка
    result = []#Итоговый список
    while True:
        line = f.readline()  # перебираем, пока есть сроки в файле
        if line:
            print(line.strip())
            company = line.split()
            #Прибыль компании, функция
            profit_company = profit(company)
            print('Прибыль компании', company[0], ':', profit(company))
            #Прибавим + 1 компанию и ее профит к общему

            if profit_company > 0:
                profit_companies += profit_company
                count_profit_companies += 1
                profit_comp_dict[company[0]] = profit_company
            else:
                not_profit_companies_dict[company[0]] = profit_company

        else:
            print('Компании, получившие прибыль, кол-во: ', count_profit_companies)

            average_profit_companies = profit_companies / count_profit_companies
            average_profit_companies_dict['Средняя прибыль для компаний с прибылью'] = average_profit_companies


            result.append(profit_comp_dict)
            result.append(average_profit_companies_dict)
            result.append(not_profit_companies_dict)
            print(result)
            break

with open('json_com_data.jon', 'w', encoding='utf-8') as f:
    json.dump(result, f)

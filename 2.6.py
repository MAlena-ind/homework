# 6.*Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента —
# номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
#     “название”: [“компьютер”, “принтер”, “сканер”],
#     “цена”: [20000, 6000, 2000],
#     “количество”: [5, 2, 7],
#     “ед”: [“шт.”]
# }

all_goods = []
quantity_goods = int(input('Введите количество товаров для заведения в базу: '))


good = list()
for ps in range(0, quantity_goods):
    good_dict={}
    good_dict['название: '] = input('Введите название товара: ')
    good_dict['цена: '] = int(input('Введите цену товара: '))
    # good_dict['количество: '] = input('Введите количество товара: ')
# good_dict['единица измерения: '] = int(input('Введите единицу измерения товара: '))
    good.append(good_dict)
 good = tuple(good)
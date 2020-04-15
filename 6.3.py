# 3)	Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
#     Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
#     В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
# (get_total_income).
#     Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).






class Worker():
    """Базовый класс Работник"""
    """Инициализация атрибутов работника.
    Доход представляет собой защищенный атрибут из словаря: оклад + 20% премия."""
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": income, "bonus": income*0.2}

class Position(Worker):
    """ Класс-наследник от Работника: Должность"""
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)


    def get_full_name(self):
        """ Полное имя сотрудника с должностью"""
        print(self.name.title(), self.surname.title(), '-', self.position)

    def get_total_income(self):
        """Доход с учетом 20% премии"""
        result = self._income["wage"] + int(self._income["bonus"])
        return result

ivanov = Position('андрей', 'иванов', 'кладовщик', 20000)
ivanov.get_full_name() #результат: Андрей Иванов - кладовщик
print(ivanov.get_total_income()) #результат: 24000

petrov = Position('сергей', 'пеТРов', 'водитель', 30000)
petrov.get_full_name()#результат: Сергей Петров - водитель
print(petrov.get_total_income()) #результат: 36000
# 4)	Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
#     Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
#     Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
#     Для классов TownCar и WorkCar переопределите метод show_speed.
#     При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
#     Выполните вызов методов и также покажите результат.




class Car():
    """Родительский класс Car (для всех машин).
    Инициализируем атрибуты машины.
    Марка, цвет и скорость вводит пользователь.
    Is_polis - по умолчанию считаем, что водитель не нарушал правила. Но если нарушал - True на наличие денежного штрафа"""
    def __init__(self, name, color, speed, is_polis = False):
        self.name = name
        self.color = color
        self.speed = int(speed)
        self.monetary_fine = is_polis

    def go(self):
        print ('Машина {} поехала.'.format(self.name))

    def stop(self):
        print('Машина {} остановилась.'.format(self.name))

    def turn(self, direction):
        print('Машина {} повернула {}.'.format(self.name, direction))

        

class TownCar(Car):
    """Дочерний класс. Остаются все атрибуты родителя +  добавляем год выпуска авто
    Сформировала 1 доч.класс вместо предложенных 4, ввиду отсутствия времени. Но с реализацией по заданию."""
    def __init__(self, name, year, color, speed, is_polis = False):
        super().__init__(name, color, speed, is_polis = False)
        self.year = year


    def show_speed(self):
        """Демонстрация скорости авто. Если скорость выше нормы, сообщение о нарушении."""
        if self.speed > 40:
            print('Скорость {}. Превышение установленной скорости.'.format(self.speed))
        else:
            print('Скорость {}.'.format(self.speed))



car_1 = TownCar('Volvo', 2002, 'red', 60, True)
print(car_1.year) #2002
car_1.go() #Машина Volvo поехала.
car_1.stop() #Машина Volvo остановилась.
car_1.turn('влево') #Машина Volvo повернула влево.
car_1.show_speed() #Скорость 60. Превышение установленной скорости.
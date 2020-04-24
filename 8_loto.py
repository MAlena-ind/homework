
import random
from abc import ABC, abstractmethod
from itertools import count

class PlayerHuman():
    """Класс Игрок-Человек. Вводит свое имя. Можно опустить данный класс, носит только информативный характер"""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Привет, ' + name + '! Сыграем в игру "ЛОТО" с компьютером. У Вас будет своя карточка. ' \
                                   'Если выпавшая цифра есть на Вашем поле - нажмите Y, если нет - N.' \
                                   'Если вы ошибетесь, будет засчитан проигрыш.' \
                                   'Начинаем'
class Computer():
    """Класс Компьютер. Приветствует соперника. Можно опустить данный класс, носит только информативный характер"""
    def __init__(self):
        print('\n' + 'Привет, я компьютер, Ваш соперник!' + '\n')


class GameCard(ABC):
    """Класс для формирования номеров для карточки +  дочерние классы Карточка человека и Карточка компьютера"""
    def __init__(self):
        """numbers - список из трех списков, каждый содержит по 9 случайно размещенных элементов: 5 цифр (разных) +
        4 пробела.
        chek - копит все номера, которые уже есть в карточке. Нигде далее не используется, только в данном классе,
        для удобства"""
        self.numbers = []
        self.check = []

    def get_numbers(self):
        """ метод для формирования списка из 3 списков. Список содержит 15 случайных неповторяющихся чисел от 1 до 90
        + 12 пробелов
        (в каждом вложенном списке 5 чисел + 4 пробела.)
        Возвращает список списков"""
        while len(self.numbers) < 3:
            line = []
            while len(line) < 5:
                n = random.randint(1, 90)
                if n in self.check:
                    continue
                else:
                    self.check.append(n)
                    line.append(n)
                    line = sorted(line)
            while len(line) < 9:
                line.insert(random.randint(0, 8), ' ')
            self.numbers.append(line)
        return self.numbers

    @abstractmethod
    def __str__(self):
        """Для каждого дочернего класса просьба описать(переопределить),
        как должен выглядеть вывод полученных номеров"""
        pass


class GameCardPlayer(GameCard, PlayerHuman):
    def __init__(self):
        """Формирование карточки игрока"""
        self.numbers = []
        self.check = []

    def __str__(self):
        return str('-' * 4 + 'ВАША КАРТОЧКА' + '-' * 4) + '\n' + '\n'.join(
            [' '.join([str(el) for el in line]) for line in self.numbers]) + '\n' + str('-' * 21)


class GameCardComputer(GameCard, Computer):
    def __init__(self):
        """Формирование карточки компьютера"""
        self.numbers = []
        self.check = []

    def __str__(self):
        return str('-' * 2 + 'КАРТОЧКА КОМПЬЮТЕРА' + '-' * 2) + '\n' + '\n'.join(
            [' '.join([str(el) for el in line]) for line in self.numbers]) + '\n' + str('-' * 21)


class NumbersBarells:

    def generator(self):
        """генератор случайных боченков из мешка"""
        for i in count(1):
            el = random.randint(1, 90)
            yield el

class Game(GameCardPlayer, GameCardComputer):
    def __init__(self, game_card_player, game_card_computer):
        """класс Игра. """
        self.received_numbers_from_bag = [] #собираем номера, которые уже достали из мешка. Входящий список пустой.
        self.game_card_player = game_card_player
        self.gkp = game_card_player.numbers  # для отслеживания формируем карточку игрока в 3 list = 3 строчки.
        # Внутренняя переменная

        self.game_card_computer = game_card_computer
        self.gcc = game_card_computer.numbers  # для отслеживания формируем карточку компьютера в 3 list = 3 строчки.
        # Внутренняя переменная
        self.counter_player = 0 #Количество совпадений (вычеркнутые из карточки игрока цифры)
        self.counter_compyter = 0 #Количество совпадений (вычеркнутые из карточки игрока цифры)


    def game(self):
        """
        бесконечный цикл:
        1. достаем боченок i
        проверяем, если есть такой номер в received_numbers_from_bag, тащим другой номер.
        если номера нет в received_numbers_from_bag, добавляем его туда, идем дальше.

        2. проверяем, сколько номеров зачеркнуто в карточке компьютера и игрока. если у кого-то 15 , значит он выиграл.
            Конец игры.

        3.  проверяем наличие номера в карточке компьютера. Если есть, увеличиваем counter_compyter на 1
         + заменяем номер на "-"

        4. ждем ответ пользователя,
        проверяем ответ пользователя... если ответ норм - продолжаем наш бесконечный цикл (увеличиваем
        counter_player на 1 + заменяем номер на "-" .
         если ответ ошибочный - конец игры. Компьютер выиграл"""
        for i in NumbersBarells.generator(self):

            if i in self.received_numbers_from_bag:
                continue
            else:
                self.received_numbers_from_bag.append(i)

            if self.counter_compyter == 15:
                print('Компьютер выиграл, конец игры!')
                break
            elif self.counter_player == 15:
                print('Поздравляем с выигрышем!')
                break

            for _ in range(0, 3):
                if i in self.gcc[_]:
                    ind = self.gcc[_].index(i)
                    self.gcc[_].pop(ind)
                    self.gcc[_].insert(ind, '-')
                    self.counter_compyter +=1

            while True:

                print('Проверяем номер', i)
                user_answer = input('У вас есть это число? ')
                if user_answer == 'y' or user_answer == 'n' or user_answer == 'Y' or user_answer == 'N':
                    break
                else:
                    print('Можно вводить только y - ЕСТЬ или n - НЕТ')
                    continue

            if user_answer == 'y' and (i in self.gkp[0] or i in self.gkp[1] or i in self.gkp[2]):
                print('Правильно, цифра зачеркнута.')
                for _ in range(0, 3):
                    if i in self.gkp[_]:
                        ind = self.gkp[_].index(i)
                        self.gkp[_].pop(ind)
                        self.gkp[_].insert(ind, '-')
                        self.counter_player += 1

                        print(game_card_player)
                        print(game_card_computer)
                continue
            elif user_answer == 'n' and not (i in self.gkp[0] or i in self.gkp[1] or i in self.gkp[2]):
                print('Правильно, продолжаем игру.')

                print(game_card_player)
                print(game_card_computer)
                continue
            elif user_answer == 'y' and not (i in self.gkp[0] or i in self.gkp[1] or i in self.gkp[2]):
                print('Неправильно, конец игры! Цифры нет.')

                break
            elif user_answer == 'n' and (i in self.gkp[0] or i in self.gkp[1] or i in self.gkp[2]):
                print('Неправильно, конец игры! Цифра есть.')

                break

#формируем двух игроков +  приветственные слова
name = input('Введите Ваше имя: ')
player_1 = PlayerHuman(name)
print(player_1)
player_2 = Computer()

#создаем экз.класса "Карточка Человека", вызываем метод получить номера (получаем уникальные номера),
# выводим с помощь переопределения __str__
game_card_player = GameCardPlayer()
game_card_player.get_numbers()
print(game_card_player)

#создаем экз.класса "Карточка Компьютера", вызываем метод получить номера (получаем уникальные номера),
# выводим с помощь переопределения __str__
game_card_computer = GameCardComputer()
game_card_computer.get_numbers()
print(game_card_computer)

#создаем экз.класса "Игра", вызываем игру
game = Game(game_card_player, game_card_computer)
game.game()

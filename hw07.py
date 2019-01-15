__author__ = 'Кильдяшев Игорь'

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html
"""
from random import randrange

def barrelGenerator():
	barrels = [i for i in range(1, 91)]
	for i in range(len(barrels)):
		yield barrels.pop(randrange(len(barrels)))

class PlayCard:
	def __init__(self, card_name):
		self.card_name = card_name
		self.b = barrelGenerator()
		self.win = False
		self.count = 15
		self.card_numbers = sorted(list(self.b)[:15])
		while len(self.card_numbers) < 27:
			self.card_numbers.insert(randrange(len(self.card_numbers)), ' '*3)

	def remove(self, number):
		try:
			self.i = self.card_numbers.index(number)
			self.card_numbers[self.i] = ' - '
			self.count -= 1
			self.win = True if self.count == 0 else False
			return True
		except ValueError:
			return False

	def __str__(self):
		self.str = '{:=^27}'.format(self.card_name) + '\n'
		for j in range(3):
			for i in range(j, 27, 3):
				self.str += '{:>3}'.format(self.card_numbers[i]) if str(self.card_numbers[i]).isdigit() else self.card_numbers[i]
			self.str += '\n'
		self.str += '{:=^27}\n'.format('Осталось {} чисел из 15'.format(self.count))
		return self.str


my = PlayCard('Ваша карточка')
comp = PlayCard('Карточка компьютера')

barrels = barrelGenerator()

for i, barrel in enumerate(barrels):
	answer = ''
	print('\n'* 25 + 'Новый боченок {}, осталось {}\n'.format(barrel, 89 - i))
	print(my)
	print(comp)
	while answer not in ('y', 'n'):
		answer = input('Зачеркнуть цифру? y/n: >')
	if (my.remove(barrel) and answer == 'n') or (my.remove(barrel) and answer == 'y'):
		print('Вы проиграли!')
		break
	_ = comp.remove(barrel)
	if my.win or comp.win:
		print('Вы выиграли! \n{}'.format(my) if my.win else 'Выиграл компьютер! \n{}'.format(comp))
		break



__author__ = 'Кильдяшев Игорь'

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import console
import os

error_message = '''
Ошибка ввода, попробуйте еще раз
'''

arg_message = '''
Введите название папки или файла
>>>'''

menu_message = '''

Выберите действие: 
1. Перейти в папку
2. Просмотреть содержимое текущей папки
3. Удалить папку
4. Создать папку
5. Создать копию указанного файла
6. Удалить указанный файл
0. Выход

Для пунктов 1,3,4,5,6 можно задать папку или файл через пробел
'''

do = {
	'1': console.ch_dir,
	'2': console.show_dir,
	'3': console.del_dir,
	'4': console.make_dir,
	'5': console.copy_file,
	'6': console.del_file,
	'0': exit,
}

print('Добро пожаловать в мою консольную утилиту!')

while True:
	s = input(menu_message + '{}>>>'.format(os.getcwd()))
	args = list(filter(lambda x: x != '', s.strip(' ').split(' ')))
	try:
		key = args[0]
	except IndexError:
		print(error_message)
	if key in ('1', '3', '4', '5', '6'):
		try:
			arg = args[1]
		except IndexError:
			arg = input(arg_message)
		do[key](arg)
	else:
		if do.get(key):
			do[key]()
		else:
			print(error_message)

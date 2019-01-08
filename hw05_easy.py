__author__ = 'Кильдяшев Игорь'

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import os
import sys
import shutil

def make_dirs():
	try:
		_ = list(map(lambda x: os.mkdir('dir_{}'.format(x)), range(1,10)))
	except OSError:
		pass

def del_dirs():
	try:
		_ = list(map(lambda x: os.rmdir('dir_{}'.format(x)), range(1,10)))
	except OSError:
		pass

def show_dirs():
	dirs = os.listdir()
	for d in dirs:
		if os.path.isdir(d):
			print(d)

def copy_exec_file():
	exec_file = sys.argv[0]
	return shutil.copyfile(exec_file,'{}_copy'.format(exec_file))

if __name__ == '__main__':
	show_dirs()
	make_dirs()
	print('Дирректории созданы: \n')
	show_dirs()
	del_dirs()
	print('Дирректории удалены: \n')
	show_dirs()
	print('Копия исполняемого файла успешно создана:\n{} '.format(copy_exec_file()))

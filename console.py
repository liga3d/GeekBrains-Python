import os
import shutil

def copy_file(file):
	full_path = file if os.path.isabs(file) else os.path.join(os.getcwd(), file)
	if os.path.isfile(full_path):
		full_path = shutil.copyfile(full_path,'{}_copy'.format(full_path))
		print('Файл {} успешно создан.'.format(full_path))
	else:
		print('{} не является файлом.'.format(full_path))

def del_file(file):
	full_path = file if os.path.isabs(file) else os.path.join(os.getcwd(), file)
	if os.path.isfile(full_path):
		s = input('''
ВНИМАНИЕ: Вы действительно хотите удалить файл? 
{}
Y - для подтверждения
>>>'''.format(full_path))
		if s == 'Y':
			os.remove(full_path)
			print('Файл {} успешно удален.'.format(full_path))
	else:
		print('{} не является файлом.'.format(full_path))

def show_dir():
	print('\nСодержимое папки {}:\n'.format(os.getcwd()))
	dirs = os.listdir()
	for d in dirs:
		print('{:<32} {:<5} {:.1f} Kb'.format(d, 'file' if os.path.isfile(d) else '<DIR>', 
			os.path.getsize(d) / 1024))

def ch_dir(dir):
	full_path = dir if os.path.isabs(dir) else os.path.join(os.getcwd(), dir) 
	if os.path.isdir(full_path):
		os.chdir(full_path)
	else:
		print('Невозможно перейти в папку {}'.format(full_path))

def make_dir(dir):
	full_path = dir if os.path.isabs(dir) else os.path.join(os.getcwd(), dir)
	try:
		os.mkdir(full_path)
		print('Папка {} успешно создана.'.format(full_path))
	except FileExistsError:
		print('Папка {} уже существует.'.format(full_path))

def del_dir(dir):
	full_path = dir if os.path.isabs(dir) else os.path.join(os.getcwd(), dir)
	if os.path.isdir(full_path):
		try:
			os.rmdir(full_path)
			print('Папка {} успешно удалена.'.format(full_path))
		except OSError:
			print('Папка {} не может быть удалена.'.format(full_path))
	else:
		print('Папка {} не существует.'.format(full_path))
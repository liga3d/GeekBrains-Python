# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

#дроби будем представлять в виде list[a, b],  a/b - дробь

def d_unpack(strs):
	drobi = []
	for str in strs:
		if ' ' in str:
			if '/' in str:
				dr = str.split(' ')[0], *str.split(' ')[1].split('/')
			else:
				dr = '0', str, '1'
		else:
			if '/' in str:
				dr = '0', *str.split('/')
			else:
				dr = '0', str, '1'
		drobi.append([int(dr[0])*int(dr[2]) + int(dr[1]), int(dr[2])])
	return drobi

def read_string(str):
	if '+' in str:
		a, b = d_unpack(inp.split(' + '))
		sign = 1
	elif '-' in str:
		a, b = d_unpack(inp.split(' - '))
		sign = -1
	return a, b, sign

def d_calc(a, b, sign):
	return [a[0] * b[1] + sign * b[0] * a[1], a[1] * b[1]]

def d_shorten(drob):
	for i in range(2, int(drob[1] ** 0.5)):
		while drob[0] % i == 0 and drob[1] % i == 0:
			drob[0], drob[1] = int(drob[0] / i), int(drob[1] / i)
	return drob

def s_output(drob):
	if drob[0] // drob[1] != 0:
		if drob[0] % drob[1] != 0:
			s = '{} {}/{}'.format(drob[0] // drob[1], drob[0] % drob[1], drob[1])
		else:
			s = '{}'.format(drob[0] // drob[1])
	else:
		s = '{}/{}'.format(drob[0], drob[1])
	return s

data = ('1/2 + 1 13/26', '5/6 + 4/7', '-2/3 - -2', '4/17 - 2 72/412')

for inp in data:
	print(inp)
	a, b, sign = read_string(inp)
	print('{}   {}'.format(s_output(d_shorten(a)), s_output(d_shorten(b))))
	print('Результат: {}\n'.format(s_output(d_shorten(d_calc(a, b, sign)))))

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

def read_file_struc(str):
	workers = []
	f = open(str,'r', encoding='cp1251')
	for line in f:
		worker = []
		for word in line.split(' '):
			if word != '':
				if word.endswith('\n'):
					worker.append(word[:-1])
				else:
					worker.append(word)
		workers.append(worker)
	f.close()
	return workers

def m_calc(*args):
	salary, norm, hours = int(args[0]), int(args[1]), int(args[2])
	if hours < norm:
		month_salary = salary * hours / norm
	else:
		month_salary = salary + (hours - norm) * 2 * salary / norm
	return month_salary

work_data = read_file_struc('workers.txt')
hours = read_file_struc('hours_of.txt')

worker_table = {'{} {}'.format(work_data[i][0], work_data[i][1]): 
	(work_data[i][2], work_data[i][3], work_data[i][4]) for i in range(1,len(work_data))}
hours_table = {'{} {}'.format(hours[i][0], hours[i][1]): hours[i][2] for i in range(1,len(hours))}

for s in worker_table.keys():
	print('{:>16}: {} {:<12} {:>4} - {:>4} зарплата: {:.2f}'.format(s, *worker_table.get(s), hours_table.get(s), 
			m_calc(worker_table.get(s)[0], worker_table.get(s)[2], hours_table.get(s))))



# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

def read_file(str):
	fruits = []
	f = open(str,'r', encoding='cp1251')
	for line in f:
		if line != '\n':
			if line.endswith('\n'):
				fruits.append(line[:-1])
			else:
				fruits.append(line)
	f.close()
	return fruits

def write_file(fruits_group, index):
 	f = open('fruits_{}.txt'.format(chr(index)), 'w', encoding='cp1251')
 	for fruit in fruits_group:
 		f.write('{}\n'.format(fruit))
 	f.close()

fruits = read_file('fruits.txt')

for i in range(ord('А'), ord('Я') + 1):
	fruits_letter = []
	for fruit in fruits:
		if fruit.startswith(chr(i)):
			fruits_letter.append(fruit)
	if len(fruits_letter) > 0:
		write_file(fruits_letter, i)

print('файлы успешно созданы!')

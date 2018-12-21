import random

__author__ = 'Кильдяшев Игорь'

list_max_count = 100
# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fr_l = ["яблоко", "банан", "киви", "арбуз","яблоко", "банан", "киви", 
		"арбуз","яблоко", "банан", "киви", "арбуз"]
i = 0
for fruit in fr_l:
	i += 1
	print('{:>2}{:.>12}'.format(i, fruit))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

l_main = []
l_del = []

for i in range(0,list_max_count):
	l_main.append(random.randrange(0,10))
	if i % 20 == 0:
		temp = random.randrange(0,10)
		while temp in l_del:
			temp = random.randrange(0,10)
		l_del.append(temp)

print('Исходный список: \n{}\n Количество элементов {}'.format(l_main, len(l_main)))
print('\nСписок удаляемых элементов: \n{}'.format(l_del))

for del_number in l_del:
	while l_main.count(del_number) > 0:
		l_main.remove(del_number)

print('\nИсходный список после удаления элементов: \n{}\nКоличество '
		'элементов: {}'.format(l_main, len(l_main)))

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

l_data = []
l_new_data = []

for i in range(0,list_max_count):
	l_data.append(random.randrange(0,100))

print('\nИсходный список: \n{}\n'.format(l_data))

for number in l_data:
	if number % 2 == 0:
		l_new_data.append(number / 4)
	else:
		l_new_data.append(number * 2)

print('Решение:')
for i in range (0,list_max_count):
	print('{:>4} -> {:<}'.format(l_data[i], l_new_data[i]))

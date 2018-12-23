import random
max_list_range = 20

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fib_l = [0, 1]
    for i in range(2, m + 1):
    	fib_l.append(fib_l[i-1] + fib_l[i-2])
    return fib_l[n:]

print(fibonacci(random.randrange(0,10),random.randrange(10,30)))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    for i in range(0, len(origin_list)):
    	for j in range(i, len(origin_list)):
    		if origin_list[j] > origin_list[i]:
    			origin_list[j], origin_list[i] = origin_list[i], origin_list[j]
    return origin_list

l = [random.randrange(-100, 100) for i in range(max_list_range)]
print('Исходный список:\n{} \n'.format(l))
print('Отсортированный список:\n{}'.format(sort_to_max(l)))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(f, list):
	new_list = []
	for i in range(0, len(list)):
		if f(list[i]):
			new_list.append(list[i])
	return new_list

l = [random.randrange(-100, 100) for i in range(max_list_range)]
print('Исходный список:\n{} \n'.format(l))
print('Отфильтрованный список:\n{}'.format(my_filter(lambda x: x > 50, l)))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

#Для определения параллелограмма будем использовать его свойсвто:
#Cумма квадратов диагоналей параллелограмма равна удвоенной сумме квадратов его двух смежных сторон.

#Нумерация точек важна и точки задаются следующим образом:
#     A2-----A3
#	 /		/
#	/	   /
#  A1-----A4
#Важно чтобы A1A3 и A2A4 были диагоналями

#функция возвращает квадрат расстояния между точками
def lng(*pnt):
	return (pnt[1][0] - pnt[0][0]) ** 2 + (pnt[1][1] - pnt[0][1]) ** 2

def is_parallelogram(*pnt):
	return lng(pnt[0], pnt[2]) + lng(pnt[1], pnt[3]) == 2 * (lng(pnt[0], pnt[1]) + lng(pnt[1], pnt[2]))

A1 = (1,1)
A2 = (2,4)
A3 = (5,4)
A4 = (4,1)

print(is_parallelogram(A1, A2, A3, A4))
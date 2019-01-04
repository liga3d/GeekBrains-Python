__author__ = 'Кильдяшев Игорь'

import functools

# Задание-1:
# Матрицы в питоне реализуются в виде вложенных списков:
# Пример. Дано:
matrix = [[1, 0, 8],
          [3, 4, 1],
          [0, 4, 2]]
          
# Выполнить поворот (транспонирование) матрицы
# Пример. Результат:
# matrix_rotate = [[1, 3, 0],
#                  [0, 4, 4],
#                  [8, 1, 2]]

# Суть сложности hard: Решите задачу в одну строку

matrix_rotate = list(zip(*[matrix[i] for i in range(3)]))
print(matrix_rotate)

# Задание-2:
# Найдите наибольшее произведение пяти последовательных цифр в 1000-значном числе.
# Выведите произведение и индекс смещения первого числа последовательных 5-ти цифр.
# Пример 1000-значного числа:
number = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""

dig_count = 5

def my_mult(num, index):
	return functools.reduce(lambda x, y: x * y, [int(num[i]) for i in range(index, index + dig_count)])

digits = list(filter(lambda x: x.isdigit(), number))
max_mult = 1
ind = 0
for i in range(0, len(digits) - dig_count):
	if my_mult(digits, i) > max_mult:
		max_mult, ind = my_mult(digits, i), i

print('{}  index:{}, {}'.format(max_mult, ind, [digits[ind + x] for x in range(5)]))

# Задание-3 (Ферзи):
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
# друг друга. Вам дана расстановка 8 ферзей на доске.
# Определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 — координаты 8 ферзей.
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.
data = ((1,5), (2,3), (3,1), (4,7), (5,2), (6,8), (7,6), (8,4))

_test_position = (3,5)

zero_matrix = [[0 for i in range(8)] for j in range(8)]

def norm_data(*args):
	data = []
	for figure in args:
		data.append(list(map(lambda x: x - 1, figure)))
	return data

def attack_matrix_pattern():
	att_matrix = [[0 for i in range(15)] for j in range(15)]
	for i, j in zip(range(15), range(15)):
		att_matrix[i][j] = 1
	for i, j in zip(range(15), range(14, -1, -1)):
		att_matrix[i][j] = 1
	for i, j in zip(range(15), [7 for _ in range(15)]):
		att_matrix[i][j] = 1
	for i, j in zip([7 for _ in range(15)], range(15)):
		att_matrix[i][j] = 1
	att_matrix[7][7] = 0
	return att_matrix

def att_pos(*args):
	att_matrix = attack_matrix_pattern()
	att_pos_matrix = zero_matrix.copy()
	for i in range(8):
		for j in range(8):
			att_pos_matrix[i][j] = att_matrix[7 + i - args[0]][7 + j - args[1]]
	return att_pos_matrix

def check_pos(home, attack):
	return att_pos(attack[0], attack[1])[home[0]][home[1]] == 1

def check_all(*args):
	result = 0
	for i in range(len(args)):
		for j in range(i + 1, len(args)):
			# строчка с print() сделана для проверки и отладки
			print('{} - {} : {}'.format(args[i], args[j], check_pos(args[i], args[j])))
			# можно ее закомментировать
			result += check_pos(args[i], args[j])
	return 'NO' if result == 0 else 'YES'

#def print_matrix(matrix):
#	for l in matrix:
#		print(l)


print(data)
print(norm_data(*data))
print(check_all(*norm_data(*data)))

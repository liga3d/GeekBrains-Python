__author__ = 'Кильдяшев Игорь'

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

from math import sqrt, acos, degrees, sin, radians

class Point:
	def __init__(self, *point):
		self.x, self.y = point

	def add(self, point):
		return Point(self.x + point.x, self.y + point.y)
	def __add__(self, point):
		return self.add(point)
	def __radd__(self, point):
		return self.add(point)
		
	def sub(self, point):
		return Point(self.x - point.x, self.y - point.y)
	def __sub__(self, point):
		return self.sub(point)
	def __rsub__(self, point):
		return point.sub(self)

	def angel(self, a, b):
		return Vector(self, a).angel(Vector(self, b))

	def length(self, point):
		return sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)
	def __str__(self):
		return '({}, {})'.format(self.x, self.y)

class Vector(Point):
	def __init__(self, a, b):
		self.start = a
		self.end = b
		self.vect = b - a
		self.x, self.y = self.vect.x, self.vect.y
	def scalar(self, vector):
		return self.x * vector.x + self.y * vector.y
	def length(self):
		return sqrt(self.x ** 2 + self.y ** 2)
	def angel(self, vector):
		self.cos = self.scalar(vector) / (self.length() * vector.length())
		return degrees(acos(self.cos))
	def __str__(self):
		return '{} --> {}'.format(self.start, self.end)

class Trapezium:
	def __init__(self, *points):
		self.a, self.b, self.c, self.d = points
		self.angel_a = self.a.angel(b, d)
		self.angel_b = self.b.angel(c, a)
		self.angel_c = self.c.angel(d, b)
		self.angel_d = self.d.angel(a, c)
	def perimetr(self):
		return self.a.length(b) + self.b.length(c) + self.c.length(d) + self.d.length(a)
	def is_trapezium(self):
		return self.angel_a == self.angel_d and self.angel_b == self.angel_c
	def square(self):
		return (self.a.length(c) ** 2 / 2) * sin(radians(Vector(a, c).angel(Vector(b, d))))
	def __str__(self):
		self.str = 'Равнобедренная трапеция\n' if self.is_trapezium() else 'Не является равнобедренной трапецией\n'
		self.str += '{} {} {} {}\nУглы:\n a={:.2f}\n b={:.2f}\n c={:.2f}\n d={:.2f}\n'.format(self.a, self.b, 
			self.c, self.d, self.angel_a, self.angel_b, self.angel_c, self.angel_d)
		self.str += 'Стороны:\n ab = {:.2f}\n bc = {:.2f}\n cd = {:.2f}\n da = {:.2f}\n'.format(self.a.length(b), 
			self.b.length(c), self.c.length(d), self.d.length(a))
		self.str += 'Периметр = {:.2f}\n'.format(self.perimetr())
		if self.is_trapezium():
			self.str += 'Площадь = {:.2f}'.format(self.square())
		return self.str

a = Point(0, 0)
b = Point(3, 15)
c = Point(17, 15)
d = Point(20, 0)

abcd = Trapezium(a, b, c, d)

print(abcd)

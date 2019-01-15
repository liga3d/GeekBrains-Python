__author__ = 'Кильдяшев Игорь'

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class Point:
	def __init__(self, point):
		self.x, self.y = point
	def length(self, point):
		return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5

class Triangel:
	def __init__(self, points):
		self.p = [Point(point) for point in points]
	def get_square(self):
		return abs(((self.p[0].x - self.p[2].x) * (self.p[1].y - self.p[2].y) - 
			(self.p[1].x - self.p[2].x) * (self.p[0].y - self.p[2].y)) / 2)
	def perimeter(self):
		return self.p[0].length(self.p[1]) + self.p[1].length(self.p[2]) + self.p[2].length(self.p[0])
	def height(self):
		return [self.get_square() * 2 / self.p[x].length(self.p[x - 1]) for x in range(3)]

s = Triangel(((1, 40), (2, 100), (0, 150)))
print(s.get_square())
print(s.perimeter())
print(s.height())



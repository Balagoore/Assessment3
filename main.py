class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        if isinstance(other, Point):
            return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


class Vector(Point):
    def length(self):
        return self.dist(Point(0, 0))

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    def __rmul__(self, other):
        return self * other

    def __str__(self):
        return f'Vector<x={self.x}, y={self.y}>'


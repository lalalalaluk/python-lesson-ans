import math

# 基礎類別
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def perimeter(self):
        pass

# 圓形類別，繼承自Shape
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# 長方形類別，繼承自Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

circle = Circle(10)
print(f"A {circle.name} with radius {circle.radius} has area {circle.area()} and perimeter {circle.perimeter()}.")

rectangle = Rectangle(10, 20)
print(f"A {rectangle.name} with width {rectangle.width} and height {rectangle.height} has area {rectangle.area()} and perimeter {rectangle.perimeter()}.")

import math
# Виконати завдання 1-3 до теми 4

# Завдання 1. Для прикладу з трикутниками (див. лаб. роботу №3) розробити
# поліморфні класи з методами:
# h. draw(self) виводить повідомлення про побудову трикутника
# i. line_width(self) виводить повідомлення про товщину лінії
# j. fill(self) виводить повідомлення про колір зафарбування
# трикутника.

class Shape:
    instances = []

    def __init__(self, x = 0, y = 0, line_width = 1, fill = "white"):
        self.x = x
        self.y = y
        self.line_width = line_width
        self.fill = fill

        Shape.instances.append(self)

    def move(self, x, y):
        self.x += x
        self.y += y

    def __str__(self):
        return f"Shape at ({self.x}, {self.y})"

    def draw(self):
        print(f"Shape at ({self.x}, {self.y}) has been drawn")
    
    def printLineWidth(self):
        print(f"Line width is {self.line_width}")
    
    def printFill(self):
        print(f"Fill color is {self.fill}")
    
class Triangle(Shape):
    def __init__(self, a, b, c, x = 0, y = 0, line_width = 1, fill = "white"):
        super().__init__(x, y, line_width, fill)
        self.a = a
        self.b = b
        self.c = c
        self.draw()
    
    def __str__(self):
        return f"Triangle at ({self.x}, {self.y}) with sides {self.a}, {self.b}, {self.c}"
    
    def perimeter(self):
        return self.a + self.b + self.c
    
    def area(self):
        p = self.perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c))**0.5
    
    def draw(self):
        print(f"Triangle with sides {self.a}, {self.b}, {self.c} has been drawn")
    
class EquiTriangle(Triangle):
    def __init__(self, a, x = 0, y = 0, line_width = 1, fill = "white"):
        super().__init__(a, a, a, x, y, line_width, fill)
        self.draw()
    
    def __str__(self):
        return f"Equilateral triangle at ({self.x}, {self.y}) with side {self.a}"
    
    def draw(self):
        print(f"Equilateral triangle with side {self.a} has been drawn")

    def area(self):
        return (3**0.5 / 4) * self.a**2
    
class RightTriangle(Triangle):
    def __init__(self, a, b, c, x = 0, y = 0, line_width = 1, fill = "white"):
        super().__init__(a, b, c, x, y, line_width, fill)
        self.draw()
    
    def __str__(self):
        return f"Right triangle at ({self.x}, {self.y}) with sides {self.a}, {self.b}, {self.c}"
    
    def draw(self):
        print(f"Right triangle with sides {self.a}, {self.b}, {self.c} has been drawn")
    
    def area(self):
        return 0.5 * self.a * self.b
    
class Rectangle(Shape):
    def __init__(self, a, b, x = 0, y = 0, line_width = 1, fill = "white"):
        super().__init__(x, y, line_width, fill)
        self.a = a
        self.b = b
        self.draw()
    
    def __str__(self):
        return f"Rectangle at ({self.x}, {self.y}) with sides {self.a}, {self.b}"
    
    def perimeter(self):
        return 2 * (self.a + self.b)
    
    def area(self):
        return self.a * self.b
    
    def draw(self):
        print(f"Rectangle with sides {self.a}, {self.b} has been drawn")
    
class Square(Rectangle):
    def __init__(self, a, x = 0, y = 0, line_width = 1, fill = "white"):
        super().__init__(a, a, x, y, line_width, fill)
        self.draw()
    
    def __str__(self):
        return f"Square at ({self.x}, {self.y}) with side {self.a}"
    
    def draw(self):
        print(f"Square with side {self.a} has been drawn")
    
    def area(self):
        return self.a**2
    
    def perimeter(self):
        return 4 * self.a
    
class Circle(Shape):
    def __init__(self, r, x = 0, y = 0, line_width = 1, fill = "white"):
        super().__init__(x, y, line_width, fill)
        self.r = r
        self.draw()
    
    def __str__(self):
        return f"Circle at ({self.x}, {self.y}) with radius {self.r}"
    
    def perimeter(self):
        return 2 * math.pi * self.r
    
    def area(self):
        return math.pi * self.r**2
    
    def draw(self):
        print(f"Circle with radius {self.r} has been drawn")

# Завдання 2. Для прикладу з колами та прямокутниками додати дочірній
# клас, що надасть можливість створювати правильні шестикутники (або
# п’ятикутники, або восьмикутники).

class RegularPolygon(Shape):
    def __init__(self, n, a, x = 0, y = 0, line_width = 1, fill = "white"):
        super().__init__(x, y, line_width, fill)
        self.n = n
        self.a = a
        self.draw()
    
    def __str__(self):
        return f"Regular polygon at ({self.x}, {self.y}) with {self.n} sides and side {self.a}"
    
    def perimeter(self):
        return self.n * self.a
    
    def area(self):
        return (self.n * self.a**2) / (4 * math.tan(math.pi / self.n))

    def draw(self):
        print(f"Regular polygon with {self.n} sides and side {self.a} has been drawn")

# Завдання 3. Для своєї предметної області розробити дочірні поліморфні
# класи. Створити функцію (поза класами), що послідовно опрацьовує
# створені об’єкти (аналогічно до def in_the_park(dog)).

class Sphere(Circle):
    def __init__(self, r, x = 0, y = 0, line_width = 1, fill = "white"):
        super().__init__(r, x, y, line_width, fill)
        self.draw()
    
    def __str__(self):
        return f"Sphere at ({self.x}, {self.y}) with radius {self.r}"
    
    def draw(self):
        print(f"Sphere with radius {self.r} has been drawn")
    
    def area(self):
        return 4 * math.pi * self.r**2
    
    def volume(self):
        return (4/3) * math.pi * self.r**3

class Tree(Shape):
    def __init__(self, h, r = 3, x = 0, y = 0, line_width = 1, fill = "green"):
        super().__init__(x, y, line_width, fill)
        self.h = h
        self.r = r
        self.draw()
    
    def __str__(self):
        return f"Tree at ({self.x}, {self.y}) with height {self.h} and radius {self.r}"
    
    def draw(self):
        print(f"Tree with height {self.h} and radius {self.r} has been drawn")

class Cube(Square):
    def __init__(self, a, x = 0, y = 0, line_width = 1, fill = "white"):
        super().__init__(a, x, y, line_width, fill)
        self.draw()
    
    def __str__(self):
        return f"Cube at ({self.x}, {self.y}) with side {self.a}"
    
    def draw(self):
        print(f"Cube with side {self.a} has been drawn")
    
    def area(self):
        return 6 * self.a**2
    
    def perimeter(self):
        return super().perimeter() * 6

    def volume(self):
        return self.a**3
    
def ShapeInfo(obj):
    print(obj)
    print(f"Coordinates: {obj.x}, {obj.y}")
    if(hasattr(obj, 'perimeter')):
        print(f"Perimeter: {obj.perimeter():.2f}")
    if(hasattr(obj, 'area')):
        print(f"Area: {obj.area():.2f}")
    if(hasattr(obj, 'volume')):
        print(f"Volume: {obj.volume():.2f}")
    obj.printLineWidth()
    obj.printFill()
    print()



sqareDefault = Square(5, fill="blue")
sqareRectange = Rectangle(5, 5, fill="blue")
sqarePolygon = RegularPolygon(4, 5, fill="blue")

hexagon = RegularPolygon(6, 5, fill="pink")
pentagon = RegularPolygon(5, 5, fill="pink")
octagon = RegularPolygon(8, 5, fill="pink")

sphere = Sphere(5, fill="red")
tree = Tree(10, fill="orange")
cube = Cube(5, fill="yellow")


print('\n\n')
for obj in Shape.instances:
    ShapeInfo(obj)
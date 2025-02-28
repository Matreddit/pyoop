import random
# Завдання 1. Розробити метод reflect_x у класі Point, що повертає нову
# точку, яка є відображенням заданої точки відносно вісі x. Нехай визначено
# клас Point:

class Point:
    """ Point class represents and manipulates x,y
    coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y


    # Завдання 2. Розробити метод reflect_x у класі Point, що повертає нову
    # точку, яка є відображенням заданої точки відносно вісі x.
    # Наприклад, Point(3, 5).reflect_x() є (3, -5)
    def reflect_x(self):
        return Point(self.x, -self.y)

    
    
    # Завдання 3. Розробити метод slope_from_origin у класі Point, що
    # повертає коефіцієнт прямої, яка проходить через початок координат та
    # задану точку. Наприклад, Point(4,10).slope_from_origin() є 2.5
    def slope_from_origin(self):
        return self.y / self.x
    
    # Завдання 4. Рівняння прямої – "y = kx + b". Коефіцієнти k і b повністю
    # описують лінію. Розробити метод get_line_to у класі Point, що повертає
    # коефіцієнти k і b прямої, яка проходить через точку-екземпляр та надану
    # точку. Наприклад,
    # Point(4, 11).get_line_to(Point(6, 15)) є (2,3)
    def get_line_to(self, p):
        k = (self.y - p.y) / (self.x - p.x)
        b = self.y - k * self.x
        return k, b


    # Завдання 5. Розробити метод description(self) та ще два методи для
    # своєї предметної області
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    def description(self):
        return f"{self.x}, {self.y}"
    
    def distance(self, p):
        return ((self.x - p.x)**2 + (self.y - p.y)**2 )**0.5
    
    def move(self, X, Y):
        self.x += X
        self.y += Y

    def getRandomNumber(self):
        if random.randint(0,2) == 0:
            return 1408
        else:
            return random.randint(0, 100)
    
    
    


# 1
p = Point(3, 4)
q = Point(6, 3)
r = Point()

# 2
print(Point(3, 5).reflect_x())

# 3
print(Point(4, 10).slope_from_origin())

# 4
print(Point(4,11).get_line_to(Point(6,15)))

# 5
print('\n5:')
print(p.description())
print(f'distance to q: {p.distance(q)}')
p.move(p.getRandomNumber(), p.getRandomNumber())
print(p)




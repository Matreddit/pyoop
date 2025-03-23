import random
# Тема 5. Перезавантаження операторів, методів та функцій
# Виконати завдання 1-4 до теми 5 (стор. 44 посібника)

# Завдання 1. Знайти в інтернеті відомості про метод __repr__().
# З’ясувати відмінності між методами __str__() та __repr__(). Навести
# приклади.

# __str__(): Це дружнє, читабельне рядкове представлення об'єкта, яке використовується для виводу користувачу.
# __repr__(): Це однозначне рядкове представлення об'єкта, яке використовується для налагодження. Зазвичай воно повертає рядок яким можна створити об'єкт.

class A:

    def __init__(self, x=0):
        self.x = x

    def __str__(self):
        return f'This is A with x = {self.x}'
    
    def __repr__(self):
        return f'A({self.x})'
    
a = A(3)
print(a) # __str__
a   # викличе repr в shell

l = [a]
print(l) # __repr__

a2 = eval(repr(a))
print(a2)




# Завдання 2. Для своєї предметної області в один із створених класів додати
# перезавантажену вбудовану функцію (для прикладу див. перезавантаження
# функцій abs() та bool() в лекції).
print("\nЗавдання 2")

class Character():
    def __init__(self, x,y, strength, agility, healthPoints, name):
        self.x = x
        self.y = y
        self.strength = strength     # броня
        self.agility = agility / 100 # ухилення %
        self.healthPoints = healthPoints
        self.name = name

    def getDamage(self, damage):
        if random.random() <= self.agility:
            print("ухильнувся")
            return
        self.healthPoints -= damage - self.strength
        if(self.healthPoints < 0):
            self.healthPoints = 0
        print(f"-{damage - self.strength} hp. Current hp: {self.healthPoints}")

    def attack(self, enemy):
        enemy.getDamage(self.strength * 10)

    def say(self):
        print(f"I am {self.name}, I have {self.strength} armor, {self.agility * 100}% agility and {self.healthPoints} hp")
    
    def __abs__(self):
        return (self.x**2 + self.y**2)**0.5 # відстань від початку координат
    
    def __bool__(self):
        return self.healthPoints > 0

phantom = Character(50, 50, 10, 50, 800, "Phantom")
print(abs(phantom))
print(bool(phantom))
for i in range(10):
    Character(0, 0, 15, 0, 5000, "Pudge").attack(phantom)
print(bool(phantom))

# Завдання 3. Знайти в інтернеті теоретичні відомості і приклади
# перезавантаження операторів:
#   а) віднімання (Subtraction, p1 - p2, p1.__sub__(p2))
#   б) множення (Multiplication, p1 * p2, p1.__mul__(p2)).

# Завдання 4. Для своєї предметної області в один із створених класів додати
# перезавантажений оператор (додавання, віднімання, множення, ділення).
print("\nЗавдання 3, 4")

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
    def __abs__(self):
        return (self.x**2 + self.y**2)**0.5

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        
        elif isinstance(other, (int, float)):
            length = (self.x**2 + self.y**2)**0.5
            if length == 0:
                z = other / (2**0.5)
                return Point(z, z)
            new_length = length + other
            scale = new_length / length
            return Point(self.x * scale, self.y * scale)
        else:
            print("Unsupported type")
        

    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        elif isinstance(other, (int, float)):
            return self + (-other)
    
    def __mul__(self, other):
        if isinstance(other, Point):
            return Point(self.x * other.x, self.y * other.y)
        elif isinstance(other, (int, float)):
            return Point(self.x * other, self.y * other)
        else:
            print("Unsupported type")

    def __truediv__(self, other):
        if isinstance(other, Point):
            return Point(self.x / other.x, self.y / other.y)
        elif isinstance(other, (int, float)):
            return Point(self.x / other, self.y / other)
        else:
            print("Unsupported type")


p1 = Point(0, 0)
p2 = Point(0, 5)
p3 = Point(5, 5)

print(f'(0, 0)+5 = {p1 + 5}, abs = {abs(p1 + 5)}')

print(f'(0, 5)+5 = {p2 + 5}, abs = {abs(p2 + 5)}')

print(f'(5, 5)+5 = {p3 + 5}, abs = {abs(p3 + 5)}')

print(f'\n(3,7)-(4,5) = {Point(3,7) - Point(4, 5)}')
print(f'(5,5)*2 = {p3 * 2}; (5,5)/2 = {p3 / 2}')
print(f'(5,5)*(0.1,0.1) = {p3 * Point(.1,.1)}; (5,5)/(0.1,0.1) = {p3 / Point(.1,.1)}')




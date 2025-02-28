# Завдання 1. Створити систему класів
# Triangle
#     EquiTriangle(Triangle)
#     RightTriangle(Triangle)


# Завдання 2. У класі Triangle розробити методи:
# a. виводить повідомлення it's just a triangle
# b. знаходить периметр трикутника
# c. знаходить площу за формулою Герона

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def say(self):
        print("It's just a triangle")
    
    def perimeter(self):
        return self.a + self.b + self.c
    
    def area(self):
        p = self.perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c))**0.5

# Завдання 3. У класі EquiTriangle розробити методи:
# d. виводить повідомлення it's an equilateral triangle
# e. знаходить площу за формулою для рівностороннього
# трикутника

class EquiTriangle(Triangle):
    def __init__(self, a):
        super().__init__(a, a, a)

    def say(self):
        print("It's an equilateral triangle")
    
    def area(self):
        return (3**0.5 / 4) * self.a**2

# Завдання 4. У класі RightTriangle розробити методи:
# f. виводить повідомлення it's a right triangle
# g. знаходить площу за формулою для прямокутного трикутника за
# двома катетами    

class RightTriangle(Triangle):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)
    
    def say(self):
        print("It's a right triangle")
    
    def area(self):
        return 0.5 * self.a * self.b

# Завдання 5. Створити три об’єкти (по одному кожного класу).

t = Triangle(3, 4, 5)
et = EquiTriangle(5)
rt = RightTriangle(3, 4, 5)

# Завдання 6. Застосувати розроблені методи до об’єктів (урахувати
# наслідування).

t.say()
print(f"Perimeter: {t.perimeter()}")
print(f"Area: {t.area()}")
print()
et.say()
print(f"Perimeter: {et.perimeter()}")
print(f"Area: {et.area()}")
print()
rt.say()
print(f"Perimeter: {rt.perimeter()}")
print(f"Area: {rt.area()}")
print()

# Завдання 7. До двох створених об’єктів застосувати функцію
# isinstance() для з’ясування приналежності об’єктів до певного класу.

print(isinstance(t, Triangle))
print(isinstance(et, Triangle))
print(isinstance(rt, Triangle))

print(isinstance(t, EquiTriangle))
print(isinstance(et, EquiTriangle))
print(isinstance(rt, EquiTriangle))

print(isinstance(t, RightTriangle))
print(isinstance(et, RightTriangle))
print(isinstance(rt, RightTriangle))
print()

# Завдання 8. Для своєї предметної області створити два дочірніх класи.
# Нехай екземпляри дочірніх класів містять нову властивість. Розробити
# методи для цих класів. Застосувати розроблені методи до об’єктів
# (урахувати наслідування).
# предметна область: комп’ютерні ігри

##########################################################################
##########################################################################
##########################################################################
##########################################################################
# redo
class PhysicsTriangle(Triangle):
    def __init__(self, a, b, c, density):
        super().__init__(a, b, c)
        self.density = density  # Щільність матеріалу
    
    def mass(self):
        return self.area() * self.density

    def say(self):
        print("It's a physics-based triangle")


class GraphicsTriangle(Triangle):
    def __init__(self, a, b, c, color):
        super().__init__(a, b, c)
        self.color = color  # Колір трикутника
    
    def change_color(self, new_color):
        self.color = new_color

    def say(self):
        print("It's a graphics-based triangle")


# Створення об'єктів
pt = PhysicsTriangle(3, 4, 5, 2.5)
gt = GraphicsTriangle(3, 4, 5, "red")

# Використання методів
pt.say()
print(f"Perimeter: {pt.perimeter()}")
print(f"Area: {pt.area()}")
print(f"Mass: {pt.mass()}")
print()

gt.say()
print(f"Perimeter: {gt.perimeter()}")
print(f"Area: {gt.area()}")
print(f"Color: {gt.color}")
gt.change_color("blue")
print(f"New Color: {gt.color}")

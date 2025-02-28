import random

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

print('t ' + str(isinstance(t, Triangle)))
print('t ' + str(isinstance(et, Triangle)))
print('t ' + str(isinstance(rt, Triangle)))

print('e ' + str(isinstance(t, EquiTriangle)))
print('e ' + str(isinstance(et, EquiTriangle)))
print('e ' + str(isinstance(rt, EquiTriangle)))

print('r ' + str(isinstance(t, RightTriangle)))
print('r ' + str(isinstance(et, RightTriangle)))
print('r ' + str(isinstance(rt, RightTriangle)))
print('\nЗавдання 8.')

# Завдання 8. Для своєї предметної області створити два дочірніх класи.
# Нехай екземпляри дочірніх класів містять нову властивість. Розробити
# методи для цих класів. Застосувати розроблені методи до об’єктів
# (урахувати наслідування).
# предметна область: комп’ютерні ігри




class Character(Triangle):
    def __init__(self, a, b, c, strength, agility, healthPoints, name):
        super().__init__(a, b, c)
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

    

phantom = Character(3, 4, 5, 10, 70, 800, "Phantom")
phantom.say()

pudge = Character(6, 8, 10, 15, 0, 5000, "Pudge")
pudge.say()
for i in range(10):
    pudge.attack(phantom)

phantom.say()


class Fountain(Triangle):
    def __init__(self, a, b, c, gameLevel):
        super().__init__(a, b, c)
        self.gameLevel = gameLevel

    def heal(self, character):
        character.healthPoints += 50 * self.gameLevel
        print(f"+50 hp. Current hp: {character.healthPoints}")

    def expand(self, character):
        character.a += self.gameLevel * 5
        character.b += self.gameLevel * 5
        character.c += self.gameLevel * 5
        print(f"Triangle expanded: a={self.a}, b={self.b}, c={self.c}")


    def say(self):
        print(f"I am Fountain, I can heal {self.gameLevel * 50} hp")

print()
fountain = Fountain(30, 30, 30, 1)
fountain.say()
fountain.heal(phantom)

print(f"Phantom's perimetr: {phantom.perimeter()}")
fountain.expand(phantom)
print(f"Phantom's perimetr: {phantom.perimeter()}")



# Тема 6. Абстракція та інкапсуляція
# Виконати завдання 1-3 до Теми 6 (стор. 61-63 посібника)

# Завдання 1. Створити класи Truck, Car та Bus, кожен з яких містить
# методи start(), stop(), accelerate(). Класи Truck, Car та Bus
# є дочірніми до абстрактного класу Automobile. Структура класів повинна
# бути такою, як показано на схемі:

# В абстрактному класі Automobile описати абстрактні методи
# start(), stop(), accelerate(), але не реалізовувати їх. У
# дочірніх класах імплементувати методи start(), stop(),
# accelerate(). Створити по одному об’єкту кожного класу.
# Застосувати до них розроблені методи.
# Урахувати, що при створенні дочірніх класів, розробнику не потрібно
# шукати методи для реалізації, їх можна бачити в абстрактному класі.
# Переконатися, що якщо в одному із підкласів (Truck, Car, Bus) не
# реалізувати один із методів, то Python автоматично видасть
# повідомлення про помилку.

import random
from abc import ABC, abstractmethod

class Automobile(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
    @abstractmethod
    def accelerate(self):
        pass

class Truck(Automobile):
    def start(self):
        print("Truck started")
    
    def stop(self):
        print("Truck is stopping")
    
    def accelerate(self):
        print("Truck is accelerating")

class Car(Automobile):
    def start(self):
        print("Car started")
    
    def stop(self):
        print("Car is stopping")
    
    def accelerate(self):
        print("Car is accelerating")

class Bus(Automobile):
    def start(self):
        print("Bus started")
    
    def stop(self):
        print("Bus is stopping")
    
    def accelerate(self):
        print("Bus is accelerating")

def l():
    print("=============================================")

truck = Truck()
car = Car()
bus = Bus()

truck.start()
truck.accelerate()
truck.stop()
l()
car.start()
car.accelerate()
car.stop()
l()
bus.start()
bus.accelerate()
bus.stop()
l()


# Завдання 2. Нехай задано програмний код:

# Зробити усі змінні в класі Robot приватними. Спробувати
# надрукувати таку змінну за межами класу.
# Змінити метод move() так, щоб використовувати приватну змінну і
# викликати його з основної програми. (Пам’ятайте про необхідність створення
# метода, який надає доступ до move() ззовні класу).
# Створити метод setter() для однієї зі змінних. Використати створений
# метод, щоб змінити значення змінної.
# Створити метод getter() для тієї самої змінної, що і метод setter().
# Використати метод getter() для доступу та виведення на екран цієї змінної.

class Robot:
    def __init__(self, name, version, price):
        self.__name = name
        self.__version = version
        self.__price = price

    def setPrice(self, price):
        self.__price = price
    def getPrice(self):
        return self.__price
    
    price = property(getPrice, setPrice)

    def move(self, speed):
        print("{} can move with speed {} m".format(self.__name, speed))

obj = Robot("Leju", "AL-PRO-E1E", 9570.0)
obj.move(100)

# print(f'private obj.name {obj.__name}')
print(f'private obj.name {obj._Robot__name}') 

obj.price = 20
print(f'price {obj.price}')

# Завдання 3. Для своєї предметної області у створених класи зробити деякі
# змінні захищеними, а деякі приватними. Створити методи setter() та
# getter() для таких змінних, використати їх в основній програмі.
# предметна область: комп'ютерні ігри
l()
l()

class Game:
    def __init__(self, title, releaseYear, price, platforms):
        self.__title = title
        self.__releaseYear = releaseYear
        self.__price = price
        self._platforms = platforms
    
    def getTitle(self):
        return self.__title
    def setTitle(self, title):
        self.__title = title
    title = property(getTitle, setTitle)
    def getReleaseYear(self):
        return self.__releaseYear
    def setReleaseYear(self, releaseYear):
        self.__releaseYear = releaseYear
    releaseYear = property(getReleaseYear, setReleaseYear)
    def getPrice(self):
        return self.__price
    def setPrice(self, price):
        self.__price = price
    price = property(getPrice, setPrice)
    def getPlatforms(self):
        return self._platforms
    def setPlatforms(self, platforms):
        self._platforms = platforms
    platforms = property(getPlatforms, setPlatforms)

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def play(self):
        pass


class SinglePlayerGame(Game):
    def __init__(self, title, releaseYear, price, platforms, mainCharacter):
        super().__init__(title, releaseYear, price, platforms)
        self.__mainCharacter = mainCharacter
    
    def getMainCharacter(self):
        return self.__mainCharacter
    def setMainCharacter(self, mainCharacter):
        self.__mainCharacter = mainCharacter
    mainCharacter = property(getMainCharacter, setMainCharacter)

    def __str__(self):
        return f"Single player game {self.title} released in {self.releaseYear} for {self.price}$"

    def play(self):
        print(f"Playing single player game {self.title} with {self.mainCharacter}")


class MultiPlayerGame(Game):
    def __init__(self, title, releaseYear, price, platforms, maxPlayers):
        super().__init__(title, releaseYear, price, platforms)
        self.__maxPlayers = maxPlayers
    
    def getMaxPlayers(self):
        return self.__maxPlayers
    def setMaxPlayers(self, maxPlayers):
        self.__maxPlayers = maxPlayers
    maxPlayers = property(getMaxPlayers, setMaxPlayers)

    def __str__(self):
        return f"Multiplayer game {self.title} released in {self.releaseYear} for {self.price}$"

    def play(self):
        print(f"Playing multiplayer game {self.title} with {self.maxPlayers} players")

hl1 = SinglePlayerGame("Half-Life", 1998, 9.99, ["PC", "PS2", "Xbox"], "Gordon Freeman")
factorio = MultiPlayerGame("Factorio", 2016, 35.0, ["PC"], 65535)
csgo = MultiPlayerGame("Counter-Strike: Global Offensive", 2012, 0.0, ["PC", "PS3", "Xbox 360"], 10)

print(hl1)
print(factorio)
print(csgo)
l()
hl1.price = 1.99
factorio.releaseYear = 2020
csgo.title = "Counter-Strike 2"
csgo.releaseYear = 2023

print(hl1)
print(factorio)
print(csgo)
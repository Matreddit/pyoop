# Завдання 1. Вибрати предметну область для створення класу відповідно до
# номера прізвища в журналі:
# # # комп’ютерні ігри

# Завдання 2. Створити клас, описати метод __init __ (), в якому
# ініціалізувати (вказати) три властивості (атрибути) об'єкта. Для
# властивостей використати мінімум 2 типи даних, наприклад, рядковий та
# цілочисловий.

class ComputerGames:

    category = "Video Game"

    def __init__(self, name, genre, year):
        self.name = name
        self.genre = genre
        self.year = year

    def show(self):
        print(f"Name: {self.name} | Genre: {self.genre} | Year: {self.year}")

# Завдання 3. Створити 5 об’єктів класу. Вивести на екран значення
# властивостей для кожного об’єкта.

game1 = ComputerGames("The Witcher 3: Wild Hunt", "Action RPG", 2015)
game2 = ComputerGames("Cyberpunk 2077", "Action RPG", 2020)
game3 = ComputerGames("The Elder Scrolls V: Skyrim", "Action RPG", 2011)
game4 = ComputerGames("Grand Theft Auto V", "Action-adventure", 2013)
game5 = ComputerGames("Red Dead Redemption 2", "Action-adventure", 2018)

game1.show()
game2.show()
game3.show()
game4.show()
game5.show()


# Завдання 4. Визначити атрибут класу. Створити умовний оператор, який
# перевіряє наявність цього атрибуту в одного з об’єктів класу.
# has attribute
if hasattr(game1, "category"):
    print("Attribute 'category' is present in game1")
else:
    print("Attribute 'category' is not present in game1")


# Завдання 5. Створити функцію, яка визначає найменше значення
# властивості (з числовим значенням) серед усіх ініціалізованих об’єктів
# класу.

def min_year(*args):
    return min(args)

print(f"Min year: {min_year(game1.year, game2.year, game3.year, game4.year, game5.year)}")
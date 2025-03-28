# Тема 7. Віджети мітка, кнопка, текстове поле
# Виконати завдання 1  до Теми 7 посібника (стор. 85-86)

# Завдання 1. Вибрати дві довільні задачі із списку наведеного нижче.
# Створити програми для їх розв’язання з використанням GUI. Віджети
# розмістити на полотні з використанням технології Grid. Додати малюнок.


# - Дано перелік континентів. Написати програму, в якій при введенні
# назви континенту виводиться список країн (2-5 назв), що розташовані
# на цьому континенті.

from tkinter import *

w = Tk()
w.title("countries by continent")
w.geometry("1090x665") 
w.resizable(0, 0)

task = '''
Введіть назву континенту, щоб дізнатися які країни на ньому розташовані.
'''

countries = {
        "африка": ["Нігерія", "Єгипет", "Південна Африка", "Кенія", "Алжир"],
        "європа": ["Данія", "Італія", "Німеччина", "Франція", "Іспанія", "Польща"],
        "азія": ["Китай", "Індія", "Японія", "Південна Корея", "Індонезія"],
        "північна америка": ["США", "Канада", "Мексика", "Гренада", "Коста-Рика"],
        "пн америка": ["США", "Канада", "Мексика", "Гренада", "Коста-Рика"],
        "південна америка": ["Бразилія", "Аргентина", "Чилі", "Колумбія", "Перу"],
        "пд америка": ["Бразилія", "Аргентина", "Чилі", "Колумбія", "Перу"],
        "австралія": ["Австралія", "Папуа-Нова Гвінея", "Фіджі", "Нова Зеландія"],
        "антарктида": ["немає"]

    }
pics = {
        "африка": "unik/Term II/Labs/.t7resources/afr.png",
        "європа": "unik/Term II/Labs/.t7resources/europe.png",
        "азія": "unik/Term II/Labs/.t7resources/asia.png",
        "північна америка": "unik/Term II/Labs/.t7resources/namer.png",
        "пн америка": "unik/Term II/Labs/.t7resources/namer.png",
        "південна америка": "unik/Term II/Labs/.t7resources/samer.png",
        "пд америка": "unik/Term II/Labs/.t7resources/samer.png",
        "австралія": "unik/Term II/Labs/.t7resources/austr.png",
        "антарктида": "unik/Term II/Labs/.t7resources/antarct.png"
}

lbl_task = Label(w, text=task, font=("Arial Bold", 16), padx=20).grid(column=0, row=0, columnspan=5, sticky=W)

lblContinent = Label(w, text="Континент: ", font=("Arial Bold", 14), padx=20).grid(column=0, row=1, sticky=E)
ent1 = Entry(w, width=20, font=("Arial", 12))
ent1.grid(column=1, row=1, columnspan=2 ,sticky=W, ipady=5)

lblCoutnries = Label(w, text="", font=("Arial Bold", 16), pady=20, padx=20)
lblCoutnries.grid(column=0, row=2, columnspan=4, sticky='ew')

img = PhotoImage(file="unik/Term II/Labs/.t7resources/none.png").zoom(2)
lbl_img = Label(w, image=img)
lbl_img.grid(column=1, row=3, rowspan=3, padx=20, pady=20)

def culcCountries():
    continent = ent1.get().lower().strip()
    result = ""
    if continent == "":
        result = "Зрада, введіть назву континенту"
    elif continent in countries:
        result = f"Країни: {', '.join(countries[continent])}"

        img = PhotoImage(file=pics[continent]).zoom(2)
        lbl_img.config(image=img)
        lbl_img.image = img
    else:
        result = "Континент не знайдено"

    if result[0] == "З" or result[1] == "о":
        lblCoutnries.config(text=result, fg="red")
    else:
        lblCoutnries.config(text=result, fg="green")
    # print(result)

btnCountries = Button(w, text="Показати", bg="green", fg="white", font=("Arial Bold", 16), command=culcCountries)
btnCountries.grid(column=3, row=1, padx=20, sticky=W)


def closeWindow():
    w.destroy()

btnExit = Button(w, text="Вихід", bg="red", fg="white", font=("Arial Bold", 16), command=closeWindow)
btnExit.grid(column=4, row=5, padx=20, sticky=SE)

lblHelp = Label(w, text="", font=("Arial Bold", 12), anchor="e", justify=LEFT)
lblHelp.grid(column=4, row=2, rowspan=3, sticky='e')
txtHelp = """
На планеті Земля є
наступні материки: 
Африка, Азія, Європа,
Пн Америка, Пд Америка,
Австралія, Антарктида.
"""
def help():
    lblHelp.config(text=txtHelp, fg="blue")
        
btnHelp = Button(w, text="Help", bg="blue", fg="white", font=("Arial Bold", 16), command=help)
btnHelp.grid(column=4, row=1, padx=20, sticky=W)

w.mainloop()
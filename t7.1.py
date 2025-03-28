# Тема 7. Віджети мітка, кнопка, текстове поле
# Виконати завдання 1  до Теми 7 посібника (стор. 85-86)

# Завдання 1. Вибрати дві довільні задачі із списку наведеного нижче.
# Створити програми для їх розв’язання з використанням GUI. Віджети
# розмістити на полотні з використанням технології Grid. Додати малюнок.


#  Дано площу основи та висоту циліндра, знайти його повну поверхню

from tkinter import *
from math import pi

w = Tk()
w.title("surface area of cylinder")
w.geometry("966x563") # 904 538 # 966 563
w.resizable(0, 0)

task = '''
Дано площу основи та висоту циліндра, знайти його повну поверхню.
'''

lbl_task = Label(w, text=task, font=("Arial Bold", 16), padx=20).grid(column=0, row=0, columnspan=4, sticky=W)

lblS = Label(w, text="площа основи = ", font=("Arial Bold", 14)).grid(column=0, row=1, sticky=E)
entS = Entry(w, width=10, font=("Arial", 12))
entS.grid(column=1, row=1, sticky=W, ipady=8)

lblH = Label(w, text="висота циліндра = ", font=("Arial Bold", 14)).grid(column=0, row=2, sticky=E)
entH = Entry(w, width=10, font=("Arial", 12))
entH.grid(column=1, row=2, sticky=W, ipady=8)

lblFullS = Label(w, text="", font=("Arial Bold", 16))
lblFullS.grid(column=0, row=4, columnspan=2)


def culcSurfaceArea():
    S = entS.get()
    h = entH.get()
    result = ""
    if S == "" or h == "":
        # lblFullS = Label(w, text="Зрада, введіть дані", font=("Arial Bold", 16)).grid(column=0, row=4)
        result = "Зрада, введіть дані"
    else:
        S = float(entS.get())
        h = float(entH.get())
        r = (S / pi) ** 0.5
        SCylinder = 2*pi*r*h + 2*S
        result = f"повна площа = {SCylinder:5.2f}"
    
    if result[0] == "З":
        lblFullS.config(text=result, fg="red")
    else:
        lblFullS.config(text=result, fg="green")
    # lblFullS = Label(w, text=result, font=("Arial Bold", 16)).grid(column=0, row=4, columnspan=3)

def closeWindow():
    w.destroy()
btnExit = Button(w, text="Exit", bg="red", fg="white", font=("Arial Bold", 16), command=closeWindow).grid(column=0, row=5, padx=20, sticky=SW)

btnCalc = Button(w, text="Calculate", bg="green", fg="white", font=("Arial Bold", 16), command=culcSurfaceArea)
btnCalc.grid(column=0, row=3, pady=14, padx=30, sticky="ew", columnspan=2)

img = PhotoImage(file="unik/Term II/Labs/.t7resources/.Ft7.1.png")
lbl_img = Label(w, image=img)
lbl_img.grid(column=3, row=1, rowspan=5, padx=20, pady=20)

w.mainloop()
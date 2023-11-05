# from tkinter import *
import random
from time import sleep

def hello_world():
    a = ["Да", "Нет", "Стоит попробовать", "Звезды говорят да", "Духи говорят нет", "Ты справишься", "Это стоит риска"]
    r = str(a[random.randint(1, len(a))])
    sleep(1) 
    my_l.config(text=r)

from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
my_l = ttk.Label(frm, text="Не уверена в своем решении?")
# my_l.grid(column=0, row=0)
my_l.pack()
my_b = ttk.Button(frm, text="Посоветуйся с магическим шаром", command=hello_world)
# my_b.grid(column=1, row=0)
my_b.pack()


# ttk.Label(frm, text=str(hello_world())).grid(column=0, row=0)

root.mainloop()
# root.quit()
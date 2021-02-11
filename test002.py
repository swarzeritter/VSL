from tkinter import *
import pymysql
from pymysql.cursors import DictCursor
import tkinter.messagebox as mb
def one():
    login = l.get()
    password = p.get()
    conn = pymysql.connect(
        host='192.168.212.101',
        user='aroot',
        password='school29',
        db='learn',
        charset='utf8mb4',
        cursorclass=DictCursor)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM account WHERE login = "+"'"+login+"'"+" and password = "+"'"+password+"'"+"")
    row = cursor.fetchone()
    if row == None:
        mb.showerror("Помилка", "Неправильно введений логін або пароль!")
    else:
       print("Найден аккаунт")
    cursor.close()
    conn.close()
root = Tk()
l=StringVar()
p=StringVar()
w = root.winfo_screenwidth() 
h = root.winfo_screenheight() 
w = (w//2) -200
h = (h//2) -200
root.title("Вход")
root.geometry('400x400+{}+{}'.format(w, h))
root.resizable(width=False, height=False)
login1 = Label(text="Введіть ім'я:")
login1.place(x=20, y=239)
password1 = Label(text="Введіть пароль:")
password1.place(x=0.1, y=290)
login2 = Entry(textvariable=l)
login2.place(x=200, y=250, anchor="c",height=20, width=200)
password2 = Entry(textvariable=p)
password2.place(x=200, y=300, anchor="c",height=20, width=200)
button = Button(text="Вход", command=one)
button.place(relx=.5, rely=.85, anchor="c",height=20, width=200)
root.mainloop()







#pymysql
#text1 = Label(text="123", font="Arial 32")
#text1.config(bd=20)
#text1.pack()


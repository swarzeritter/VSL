from tkinter import *
import pymysql
import os
import sys
from pymysql.cursors import DictCursor
import tkinter.messagebox as mb
def main():
    global root
    username=str(login)
    passw=str(password)
    cursor = conn.cursor()
    cursor.execute("SELECT ftppass FROM account WHERE login = "+"'"+login+"'"+"")
    ftppass = cursor.fetchone()
    text = str(ftppass)
    stepone = text.replace("{'ftppass': '", "")
    steptwo = stepone.replace("'}", "")
    file = open(os.path.abspath(os.path.dirname(sys.argv[0]))+"\config\VSC-online\.vscode\sftp.json", "w")
    file.write('{ \n    "name": "School29",\n    "host": "192.168.212.101",\n    "protocol": "ftp",\n    "port": 21,\n    "username": "'+username+'",\n    "password": "'+steptwo+'",\n    "remotePath": "/",\n    "uploadOnSave": true\n}')
    file.close()
    root.destroy() 
    root = Tk()
    root.overrideredirect(1)
    l=StringVar()
    p=StringVar()
    w = root.winfo_screenwidth() 
    h = root.winfo_screenheight() 
    w = (w//2) -200
    h = (h//2) -200
    root.geometry('400x400+{}+{}'.format(w, h))
    root.title("main")
    button = Button(text="Выход", command=ex)
    button.place(relx=.5, rely=.85, anchor="c",height=20, width=200)
    button2 = Button(text="инструкция", command=instruction)
    button2.place(relx=.8, rely=.75, anchor="c",height=20, width=100)
    root.mainloop()
def invite():
    global login
    global password
    global cursor
    global conn
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
    cursor.close()
    if row == None:
        mb.showerror("Помилка", "Неправильно введений логін або пароль!")
    else:
        cursor = conn.cursor()
        cursor.execute("UPDATE account SET `status`= 'online' WHERE login = "+"'"+login+"'"+"")
        conn.commit()
        main()
def ex():
    global cursor
    global conn
    file = open(os.path.abspath(os.path.dirname(sys.argv[0]))+"\config\VSC-online\.vscode\sftp.json", "w")
    file.write('{ \n    "name": "School29",\n    "host": "0",\n    "protocol": "ftp",\n    "port": 21,\n    "username": "0",\n    "password": "0",\n    "remotePath": "/",\n    "uploadOnSave": true\n}')
    file.close()
    cursor = conn.cursor()
    cursor.execute("UPDATE account SET `status`= 'offline' WHERE login = "+"'"+login+"'"+"")
    conn.commit()
    conn.close()
    root.destroy()
def instruction():
    os.startfile(os.path.abspath(os.path.dirname(sys.argv[0]))+"/config/instruction.txt")
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
button = Button(text="Вход", command=invite)
button.place(relx=.5, rely=.85, anchor="c",height=20, width=200)
root.mainloop()





#pymysql
#text1 = Label(text="123", font="Arial 32")
#text1.config(bd=20)
#text1.pack()
#conn = pymysql.connect(
        #host='192.168.212.101',
        #user='aroot',
        #password='school29',
        #db='learn',
        #charset='utf8mb4',
        #cursorclass=DictCursor)


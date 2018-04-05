from tkinter import *

def plus():
    n1 = int(e1.get())
    n2 = int(e2.get())
    t1.config(text = str(n1 + n2))

def minus():
    n3 = int(e3.get())
    n4 = int(e4.get())
    t1.config(text = str(n3 - n4))

def umn():
    n5 = int(e5.get())
    n6 = int(e6.get())
    t1.config(text = str(n5 * n6))

def podel():
    n7 = int(e7.get())
    n8 = int(e8.get())
    t1.config(text = str(n7 / n8))

def avg():
    n9 = int(e9.get())
    n10 = int(e10.get())
    n11 = int(e11.get())
    L = (n9 + n10 + n11)
    a = (n9, n10, n11)
    avg = float(L) / len(a)
    t1.config(text = str(avg))

def minimum():
    n12 = int(e12.get())
    n13 = int(e13.get())
    n14 = int(e14.get())
    #minimum = min(n12, n13, n14)
    t1.config(text=str(min(n12, n13, n14)))

def x2():
    n15 = int(e15.get())
    t1.config(text=str(pow(n15,2)))

window = Tk()
window.geometry('1080x720')
window.title('Калькулятор by Vad1mka')



t1 = Label(window, text='Здесь будет результат', fg='blue')
t1.config(font=('Verdana', 25))
t1.pack()

e1 = Entry(window,  width = 24, bg='white', fg='black')
e1.place(x=140,y=160)
e1.pack(padx="14", pady="1")

e2 = Entry(window, width = 24, bg='white', fg='black')
e2.place(x=20,y=50)
e2.pack(padx="7", pady="1")


b1 = Button(window, text='Добавить', command=plus)
b1.config(width=20, height=2, bg='green', fg='blue')
b1.pack(padx="14", pady="1")

e3 = Entry(window, width = 24, bg='white', fg='black')
e3.pack(padx="14", pady="1")

e4 = Entry(window, width = 24, bg='white', fg='black')
e4.pack(padx="14", pady="1")

b2 = Button(window, text='Отнять', command=minus)
b2.config(width=20, height=2, bg='green', fg='blue')
b2.pack(padx="14", pady="1")

e5 = Entry(window, width = 24, bg='white', fg='black')
e5.pack(padx="14", pady="1")

e6 = Entry(window, width = 24, bg='white', fg='black')
e6.pack(padx="14", pady="1")

b3 = Button(window, text='Умножить', command=umn)
b3.config(width=20, height=2, bg='green', fg='blue')
b3.pack(padx="14", pady="1")

e7 = Entry(window, width = 24, bg='white', fg='black')
e7.pack(padx="14", pady="1")

e8 = Entry(window, width = 24, bg='white', fg='black')
e8.pack(padx="14", pady="1")

b4 = Button(window, text='Поделить', command=podel)
b4.config(width=20, height=2, bg='green', fg='blue')
b4.pack(padx="14", pady="1")

e9 = Entry(window, width = 24, bg='white', fg='black')
e9.pack(padx="14", pady="1")

e10 = Entry(window, width = 24, bg='white', fg='black')
e10.pack(padx="14", pady="1")

e11 = Entry(window, width = 24, bg='white', fg='black')
e11.pack(padx="14", pady="1")

b5 = Button(window, text='Среднее число', command=avg)
b5.config(width=20, height=2, bg='green', fg='blue')
b5.pack(padx="14", pady="1")

e12 = Entry(window, width = 24, bg='white', fg='black')
e12.pack(padx="14", pady="1")

e13 = Entry(window, width = 24, bg='white', fg='black')
e13.pack(padx="7", pady="1")

e14 = Entry(window, width = 24, bg='white', fg='black')
e14.pack(padx="7", pady="1")

b6 = Button(window, text='Минимум', command=minimum)
b6.config(width=20, height=2, bg='green', fg='blue')
b6.pack(padx="14", pady="1")

e15 = Entry(window, width = 24, bg='white', fg='black')
e15.pack(padx="7", pady="1")

b6 = Button(window, text='x^2 = ', command=x2)
b6.config(width=20, height=2, bg='green', fg='blue')
b6.pack(padx="14", pady="1")

window.mainloop()
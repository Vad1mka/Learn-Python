from tkinter import *

def hello():
    n1 = int(e1.get())
    n2 = int(e2.get())
    mult = n1 + n2
    t1.config(text = str(mult))

def hello2():
    n3 = int(e3.get())
    n4 = int(e4.get())
    minus = n3 - n4
    t1.config(text = str(minus))

def hello3():
    n5 = int(e5.get())
    n6 = int(e6.get())
    umn = n5 * n6
    t1.config(text = str(umn))

def hello4():
    n7 = int(e7.get())
    n8 = int(e8.get())
    podel = n7 / n8
    t1.config(text = str(podel))

def hello5():
    n9 = int(e9.get())
    n10 = int(e10.get())
    n11 = int(e11.get())
    L = (n9 + n10 + n11)
    a = (n9, n10, n11)
    avg = float(L) / len(a)
    t1.config(text = str(avg))

def hello6():
    n12 = int(e12.get())
    n13 = int(e13.get())
    n14 = int(e14.get())
    minimum = min(n12, n13, n14)
    t1.config(text=str(minimum))

def hello7():
    for()

window = Tk()
window.geometry('1080x720')
window.title('Калькулятор by Vad1mka')


t1 = Label(window, text='Здесь будет результат', fg='blue')
t1.config(font=('Verdana', 25))
t1.pack()

e1 = Entry(window,  width = 24, bg='white')
e1.pack()

e2 = Entry(window, width = 24, bg='white')
e2.pack()


b1 = Button(window, text='Добавить', command=hello)
b1.config(width=20, height=2, bg='green', fg='blue')
b1.pack()

e3 = Entry(window, width = 24, bg='white')
e3.pack()

e4 = Entry(window, width = 24, bg='white')
e4.pack()

b2 = Button(window, text='Отнять', command=hello2)
b2.config(width=20, height=2, bg='green', fg='blue')
b2.pack()

e5 = Entry(window, width = 24, bg='white')
e5.pack()

e6 = Entry(window, width = 24, bg='white')
e6.pack()

b3 = Button(window, text='Умножить', command=hello3)
b3.config(width=20, height=2, bg='green', fg='blue')
b3.pack()

e7 = Entry(window, width = 24, bg='white')
e7.pack()

e8 = Entry(window, width = 24, bg='white')
e8.pack()

b4 = Button(window, text='Поделить', command=hello4)
b4.config(width=20, height=2, bg='green', fg='blue')
b4.pack()

e9 = Entry(window, width = 24, bg='white')
e9.pack()

e10 = Entry(window, width = 24, bg='white')
e10.pack()

e11 = Entry(window, width = 24, bg='white')
e11.pack()

b5 = Button(window, text='Среднее число', command=hello5)
b5.config(width=20, height=2, bg='green', fg='blue')
b5.pack()

e12 = Entry(window, width = 24, bg='white')
e12.pack()

e13 = Entry(window, width = 24, bg='white')
e13.pack()

e14 = Entry(window, width = 24, bg='white')
e14.pack()

b6 = Button(window, text='Минимум', command=hello6)
b6.config(width=20, height=2, bg='green', fg='blue')
b6.pack()




window.mainloop()
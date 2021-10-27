from tkinter import *

root = Tk()
root.title("Calculator")

screen = Entry(root, width=35, borderwidth=5)
screen.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
  current = screen.get()
  screen.delete(0, END)
  screen.insert(0, str(current) + str(number))

def button_clear():
  screen.delete(0, END)

def button_add():
  number1 = screen.get()

  global first_num
  first_num = int(number1)

  global functioncheck
  functioncheck = "add"

  screen.delete(0, END)

def button_subtract():
  number1 = screen.get()

  global first_num
  first_num = int(number1)

  global functioncheck
  functioncheck = "subtract"

  screen.delete(0, END)

def button_divide():
  number1 = screen.get()

  global first_num
  first_num = int(number1)

  global functioncheck
  functioncheck = "divide"

  screen.delete(0, END)

def button_multiply():
  number1 = screen.get()

  global first_num
  first_num = int(number1)

  global functioncheck
  functioncheck = "multiply"

  screen.delete(0, END)

def button_equal():
  second_num = int(screen.get())

  screen.delete(0, END)

  if functioncheck == "add":
    screen.insert(0, first_num + second_num)
  if functioncheck == "subtract":
    screen.insert(0, first_num - second_num)
  if functioncheck == "divide":
    screen.insert(0, first_num / second_num)
  if functioncheck == "multiply":
    screen.insert(0, first_num * second_num)
  

button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))

button_equal = Button(root, text="=", padx=40, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=26.5, pady=20, command=button_clear)

button_add = Button(root, text="+", padx=40, pady=20, command=button_add)
button_subtract = Button(root, text="-", padx=40, pady=20, command=button_subtract)
button_divide = Button(root, text="/", padx=40, pady=20, command=button_divide)
button_multiply = Button(root, text="x", padx=40, pady=20, command=button_multiply)

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=0)

button_equal.grid(row=5, column=0)
button_clear.grid(row=6, column=1)

button_add.grid(row=4, column=1)
button_subtract.grid(row=4, column=2)
button_divide.grid(row=5, column=2)
button_multiply.grid(row=5, column=1)

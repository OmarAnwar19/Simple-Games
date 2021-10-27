from tkinter import *
from tkinter import messagebox
import random

main = Tk()
main.title("Tic Tac Toe")

def disableall():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

def check_win():
    global win
    win = False

    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")

        win = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations, X Wins!")
        disableall()
    if b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")

        win = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations, X Wins!")
        disableall()
    if b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")

        win = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations, X Wins!")
        disableall()
    if b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")

        win = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations, X Wins!")
        disableall()
    if b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")

        win = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations, X Wins!")
        disableall()
    if b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")

        win = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations, X Wins!")
        disableall()
    if b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")

        win = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations, X Wins!")
        disableall()
    if b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")

        win = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations, X Wins!")
        disableall()

    if b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")

        win = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations, O Wins!")
        disableall()
    if b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")

        win = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations, O Wins!")
        disableall()
    if b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")

        win = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations, O Wins!")
        disableall()
    if b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")

        win = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations, O Wins!")
        disableall()
    if b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")

        win = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations, O Wins!")
        disableall()
    if b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")

        win = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations, O Wins!")
        disableall()
    if b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")

        win = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations, O Wins!")
        disableall()
    if b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")

        win = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations, O Wins!")
        disableall()

def b_click(b):
    global xclick, counter

    if b["text"] == " " and xclick == True:
        b["text"] = "X"
        b.config(bg="red")
        xclick = False
        counter += 1
        check_win()
    elif b["text"] == " " and xclick == False:
        b["text"] = "O"
        b.config(bg="yellow")
        xclick = True
        counter += 1
        check_win()
    else:
        messagebox.showerror("Tic Tac Toe", "Invalid input.\nPlease choose another box.")

    if counter == 9 and win == False:
        messagebox.showinfo("Tic Tac Toe", "X and O tie.\nNo one wins.")
        disableall()

def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global xclick, counter

    counter = 0

    b1 = Button(main, text=" ", font=("Helvetica", 20), height=3, width=6, bg="silver", command=lambda: b_click(b1))
    b2 = Button(main, text=" ", font=("Helvetica", 20), height=3, width=6, bg="silver", command=lambda: b_click(b2))
    b3 = Button(main, text=" ", font=("Helvetica", 20), height=3, width=6, bg="silver", command=lambda: b_click(b3))

    b4 = Button(main, text=" ", font=("Helvetica", 20), height=3, width=6, bg="silver", command=lambda: b_click(b4))
    b5 = Button(main, text=" ", font=("Helvetica", 20), height=3, width=6, bg="silver", command=lambda: b_click(b5))
    b6 = Button(main, text=" ", font=("Helvetica", 20), height=3, width=6, bg="silver", command=lambda: b_click(b6))

    b7 = Button(main, text=" ", font=("Helvetica", 20), height=3, width=6, bg="silver", command=lambda: b_click(b7))
    b8 = Button(main, text=" ", font=("Helvetica", 20), height=3, width=6, bg="silver", command=lambda: b_click(b8))
    b9 = Button(main, text=" ", font=("Helvetica", 20), height=3, width=6, bg="silver", command=lambda: b_click(b9))

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

    bolnum = random.randint(0, 1)
    if bolnum == 0:
        xclick = True
        messagebox.showinfo("Tic Tac Toe", "X starts")
    elif bolnum == 1:
        xclick = False
        messagebox.showinfo("Tic Tac Toe", "O starts")

mainmenu = Menu(main)
main.config(menu=mainmenu)

options_menu = Menu(mainmenu, tearoff=False)
mainmenu.add_cascade(label="Menu", menu=options_menu)
options_menu.add_command(label="Reset", command=reset)
options_menu.add_command(label="Exit", command=main.destroy)

reset()
main.mainloop()

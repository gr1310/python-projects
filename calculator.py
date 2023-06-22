#import tkinter
from tkinter import *
root= Tk()
root.geometry("400x430")

#width, height
root.minsize(400,430)
root.maxsize(400,430)

#title and background colour
root.title("Calculator")
root.configure(bg="#878787")

#heading
heading=Label(text="Calculator",bg="dark grey",fg="black",height="2",width="400",font=("Times",16,"bold")).pack()
Label(root,text="",bg="#878787").pack()     #line space

input_text= StringVar()

expression=""

#for the expression to be displayed after pressing keys
def button_click(i):
    global expression
    expression = expression + str(i)
    input_text.set(expression)

#for clearing whole expression
def button_clear():
    global expression
    expression=""
    input_text.set("")

#for calculating the written expression
def button_calcuates():
    global expression
    try:
        result=str(eval(expression))
    except ZeroDivisionError:
        result="Error"
        print("You can't divide by zero!")
    input_text.set(result)
    expression=result

#for evaluationg square of a number
def x2():
    global expression
    expression=str(pow(float(eval(expression)),2))
    input_text.set(expression)

#for square root of a number
def x1_2():
    global expression
    expression=str((float(eval(expression))^(0.5)))
    input_text.set(expression)

#for additive inverse of a number
def x_1():
    global expression
    expression=str(1/(float(eval(expression))))
    input_text.set(expression)

#for multiplicative inverse of a number
def inverse():
    global expression
    expression=str(-1*(float(eval(expression))))
    input_text.set(expression)

#frame for the text field
input_frame= Frame(root,width=400,height=50,bd = 0, highlightbackground = "white", highlightcolor = "white", highlightthickness = 1)
input_frame.pack(side=TOP)

#text field
input_field = Entry(input_frame, font = ('arial', 18, 'bold'), textvariable = input_text, width = 29,justify = RIGHT)
input_field.grid(row = 0, column = 0)
input_field.pack(ipady = 10, ipadx=3)

#line space
Label(root,text="",bg="#878787").pack()

#frame for the buttons
btns_frame = Frame(root, width = 400, height =350, bg = "white")
btns_frame.pack()

#buttons
clear = Button(btns_frame, text = "Clear", width = 32, height = 3, bd = 0, fg="white",bg = "#5A5A5A", command = lambda: button_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)

rem=Button(btns_frame, text = "remainder", fg = "white", width = 10, height = 3, bd = 0, bg = "#555555", command = lambda: button_click("%")).grid(row = 0, column = 4, padx = 1, pady = 1)

divide = Button(btns_frame, text = "/", fg = "white", width = 10, height = 3, bd = 0, bg = "#555555", command = lambda: button_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)

seven = Button(btns_frame, text = "7", fg = "white", width = 10, height = 3, bd = 0, bg = "#333333", cursor = "hand2", command = lambda: button_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)

eight = Button(btns_frame, text = "8", fg = "white", width = 10, height = 3, bd = 0, bg = "#333333", cursor = "hand2", command = lambda: button_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)

nine = Button(btns_frame, text = "9", fg = "white", width = 10, height = 3, bd = 0, bg = "#333333", cursor = "hand2", command = lambda: button_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)

inv = Button(btns_frame, text = "-x", fg = "white", width = 10, height = 3, bd = 0, bg = "#444444", cursor = "hand2", command = lambda: inverse()).grid(row = 1, column = 3, padx = 1, pady = 1)

multiply = Button(btns_frame, text = "*", fg = "white", width = 10, height = 3, bd = 0, bg = "#555555", cursor = "hand2", command = lambda: button_click("*")).grid(row = 1, column = 4, padx = 1, pady = 1)

four = Button(btns_frame, text = "4", fg = "white", width = 10, height = 3, bd = 0, bg = "#333333", cursor = "hand2", command = lambda: button_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)

five = Button(btns_frame, text = "5", fg = "white", width = 10, height = 3, bd = 0, bg = "#333333", cursor = "hand2", command = lambda: button_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)

six = Button(btns_frame, text = "6", fg = "white", width = 10, height = 3, bd = 0, bg = "#333333", cursor = "hand2", command = lambda: button_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)

x1 = Button(btns_frame, text = "1/x", fg = "white", width = 10, height = 3, bd = 0, bg = "#444444", cursor = "hand2", command = lambda: x_1()).grid(row = 2, column = 3, padx = 1, pady = 1)

minus = Button(btns_frame, text = "-", fg = "white", width = 10, height = 3, bd = 0, bg = "#555555", cursor = "hand2", command = lambda: button_click("-")).grid(row = 2, column = 4, padx = 1, pady = 1)

one = Button(btns_frame, text = "1", fg = "white", width = 10, height = 3, bd = 0, bg = "#333333", cursor = "hand2", command = lambda: button_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)

two = Button(btns_frame, text = "2", fg = "white", width = 10, height = 3, bd = 0, bg = "#333333", cursor = "hand2", command = lambda: button_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)

three = Button(btns_frame, text = "3", fg = "white", width = 10, height = 3, bd = 0, bg = "#333333", cursor = "hand2", command = lambda: button_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)

plus = Button(btns_frame, text = "+", fg = "white", width = 10, height = 3, bd = 0, bg = "#555555", cursor = "hand2", command = lambda: button_click("+")).grid(row = 3, column = 4, padx = 1, pady = 1)

x12 = Button(btns_frame, text = "x^1/2", fg = "white", width = 10, height = 3, bd = 0, bg = "#444444", cursor = "hand2", command = lambda: x1_2()).grid(row = 3, column = 3, padx = 1, pady = 1)

zero = Button(btns_frame, text = "0", fg = "white", width = 21, height = 3, bd = 0, bg = "#333333", cursor = "hand2", command = lambda: button_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)

point = Button(btns_frame, text = ".", fg = "white", width = 10, height = 3, bd = 0, bg = "#555555", cursor = "hand2", command = lambda: button_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)

x_2 = Button(btns_frame, text = "x^2", fg = "white", width = 10, height = 3, bd = 0, bg = "#444444", cursor = "hand2", command = lambda: x2()).grid(row = 4, column = 3, padx = 1, pady = 1)

equals = Button(btns_frame, text = "=", fg = "white", width = 10, height = 3, bd = 0, bg = "#767676", cursor = "hand2", command = lambda: button_calcuates()).grid(row = 4, column = 4, padx = 1, pady = 1)

root.mainloop()
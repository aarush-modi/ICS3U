#Author: Aarush Modi
#Date: 4/1/2021
#Purpose: Display shapes on a GUI
from tkinter import *

def Create():
    if shape.get() == 0 and hollow.get() == 0: 
        for Counter1 in range(size.get()):
            for Counter1 in range(size.get()-1):
                textOutput.insert(END, "* ")
            textOutput.insert(END, "*" + "\n")

    elif shape.get() == 0 and hollow.get() == 1:
        for Counter1 in range(size.get()-1):
            textOutput.insert(END, "* ")
        textOutput.insert(END, "*" + "\n")
        for Counter1 in range(size.get()-2):
            textOutput.insert(END, "* ")
            for Counter1 in range(size.get()-2):
                textOutput.insert(END, "  ")
            textOutput.insert(END, "*" + "\n")
        for Counter1 in range(size.get()-1):
            textOutput.insert(END, "* ")
        textOutput.insert(END, "*" + "\n")

    elif shape.get() == 1 and hollow.get() == 0: 
        strLine = ""
        for Counter1 in range(size.get()):
            strLine = strLine + "* "
            textOutput.insert(END, strLine + "\n")

    elif shape.get() == 1 and hollow.get() == 1: 
        textOutput.insert(END, "*" + "\n")
        strLine = "*"
        strLine2 = ""
        strLine = strLine + " "
        strLine2 = strLine + "*"
        textOutput.insert(END, strLine2 + "\n")
        for Counter1 in range(size.get()-3):
            strLine = strLine + "  "
            strLine2 = strLine + "*"
            textOutput.insert(END, strLine2 + "\n")
        for Counter1 in range(size.get()-1):
            textOutput.insert(END, "* ")
        textOutput.insert(END, "*" + "\n")
        
    elif shape.get() == 2 and hollow.get() == 0: 
        for Counter1 in range(0,size.get(),2):
            textOutput.insert(END, " "*(size.get()-Counter1-1) + "* "*(Counter1+1) + "\n")
        for Counter2 in range(size.get()-2, 0, -2):
            textOutput.insert(END, " "*(size.get()-Counter2) + "* "*(Counter2) + "\n")

    elif shape.get() == 2 and hollow.get() == 1: #hollow diamond
        textOutput.insert(END, "  "*(size.get()//2) + "*" + "  "*(size.get()//2) + "\n")
        for Counter1 in range(2,size.get(),2):
            textOutput.insert(END, " "*(size.get()- Counter1-1) + "* " + "  "*(Counter1-1) + "* " + "\n")
        for Counter2 in range(size.get()-2, 2, -2):
            textOutput.insert(END, " "*(size.get()-Counter2) + "* " + "  "*(Counter2-2) + "* " + "\n")
        textOutput.insert(END, "  "*(size.get()//2) + "*" + "  "*(size.get()//2) + "\n")
    textOutput.insert(END, " " + "\n")

def Clear():
    textOutput.delete(1.0, "end")

#MAIN

Display = Tk()

shape = IntVar()
hollow = IntVar()
size = IntVar()

ShapeFrame = LabelFrame(Display, width=25, height=30)
HollowFrame = LabelFrame(Display, width=25, height=30)
Square = Radiobutton(ShapeFrame, text = "Square", font = 15, variable = shape, value = 0)
Triangle = Radiobutton(ShapeFrame, text = "Triangle", font = 15, variable = shape, value = 1)
Diamond = Radiobutton(ShapeFrame, text = "Diamond", font = 15, variable = shape, value = 2)
Fill = Radiobutton(HollowFrame, text = "Filled", font = 15, variable = hollow, value = 0)
Hollow = Radiobutton(HollowFrame, text = "Hollow", font = 15, variable = hollow, value = 1)
buttonCreate = Button(Display, text = "Create shape", width=25, height=2, command=lambda: Create())
buttonClear = Button(Display, text = "Clear shape", width=25, height=2, command=lambda: Clear())
textOutput = Text(Display, width=50, height=24)
size = Scale (Display, from_ = 3, to = 23, resolution = 1, orient = HORIZONTAL)
size.set(50)

ShapeFrame.grid(row=1, column=2, pady=10)
Square.grid(row=1, column=1, sticky=W)
Triangle.grid(row=2, column=1, sticky=W)
Diamond.grid(row=3, column=1, sticky=W)
HollowFrame.grid(row=1, column=1, pady=10)
Fill.grid(row=1, column=2, sticky=W)
Hollow.grid(row=2, column=2, sticky=W)
size.grid(row=3, column=1, pady=10)
buttonClear.grid(row=2, column=2)
buttonCreate.grid(row=3, column=2)
textOutput.grid(row=5, column=1, columnspan=2)

mainloop()



# Author: Aarush Modi
# Date: April 3, 2021
# Purpose: Make a domino class for OOP1

import random
from tkinter import *

# Author: Aarush Modi
# Date: April 3, 2021
# Purpose: Make a domino class for OOP1
# Data Elements: Value, Gap, Size, Diameter, Orientation, Face
# Methods:
# Initalize data elements (__init__)
# Return domino value as string (__str__)
# Gets input from the user for domino(getValue)
# Sets the input as domino value (setValue)
# Reverse value of domino (flip)
# Sets orientation  of domino [vertical/horizontal] (setOrientation)
# Sets size of domino (setSize)
# Sets if domino is faced up (setFace)
# Randomizes the value (randomize)
# Creates domino (draw)
#Dependancies: Tkinter, Random

class Domino:
    # AUTHOR: Aarush Modi
    # DATE: April 3, 2021
    # PURPOSE: Initalize data elements
    # INPUTS: Value, Size, Orientation, Face
    # OUTPUTS: N/A
    def __init__(self, value=-1, size=60, orientation="Horizontal", faceup="Yes"):
        if value <= 0 or value > 66 or value // 10 > 6 or value % 10 > 6:
            self.randomize()
        else:
            self.value = value

        if size >= 30 and size <= 100:
            self.size = size
        else:
            self.size  = 30

        if str(orientation) == "Horizontal" or str(orientation) == "Vertical":
            self.orientation = orientation
        else:
            self.orientation = "Vertical"

        if str(faceup) == "Yes" or str(faceup) == "No":
            self.faceup = faceup
        else:
            self.faceup = "Yes"

        self.diameter = self.size // 5
        self.gap = self.diameter // 2

    # AUTHOR: Aarush Modi
    # DATE: April 3, 2021
    # PURPOSE: Return domino value as string
    # INPUTS: N/A
    # OUTPUTS: N/A
    def __str__(self):
        strValue = str(self.value)
        return strValue

    # AUTHOR: Aarush Modi
    # DATE: April 3, 2021
    # PURPOSE:  Gets input from the user for domino
    # INPUTS: N/A
    # OUTPUTS: N/A
    def getValue(self):
        self.value = input("Please give the domino a value between 0-66, make sure none of the digits are greater than 6: ")
        while self.value.isdigit() == False or self.value < 0 or self.value > 67:
            self.value = input("Please give the domino a value between 0-66, make sure none of the digits are greater than 6: ")
        self.value = int(self.value)

    # AUTHOR: Aarush Modi
    # DATE: April 3, 2021
    # PURPOSE: Sets the input as domino value
    # INPUTS: Value
    # OUTPUTS: N/A
    def setValue(self, value):
        if value <= 0 or value > 66 or value // 10 > 6 or value % 10 > 6:
            self.randomize()
        else:
            self.value = value

    # AUTHOR: Aarush Modi
    # DATE: April 3, 2021
    # PURPOSE: Reverse value of domino
    # INPUTS: N/A
    # OUTPUTS: N/A
    def flip(self):
        self.value = self.value // 10 + (self.value - self.value // 10 * 10) * 10

    # AUTHOR: Aarush Modi
    # DATE: April 3, 2021
    # PURPOSE: Sets orientation  of domino
    # INPUTS: Orientation
    # OUTPUTS: N/A
    def setOrientation(self, orientation):
        if str(orientation) == "Horizontal" or str(orientation) == "Vertical":
            self.orientation = orientation
        else:
            self.orientation = "Vertical"

    # AUTHOR: Aarush Modi
    # DATE: April 3, 2021
    # PURPOSE: Sets size of domino
    # INPUTS: Size
    # OUTPUTS: N/A
    def setSize(self, size=30):
        if size >= 30 and size <= 100:
            self.size = size
        else:
            self.size = 30
        self.diameter = self.size // 5
        self.gap = self.diameter // 2

    # AUTHOR: Aarush Modi
    # DATE: April 3, 2021
    # PURPOSE: Sets if domino is faced up
    # INPUTS: Faceup
    # OUTPUTS: N/A
    def setFace(self, faceup):
        if str(faceup) == "Yes" or str(faceup) == "No":
            self.faceup = faceup
        else:
            self.faceup = "Yes"

    # AUTHOR: Aarush Modi
    # DATE: April 3, 2021
    # PURPOSE: Randomizes the domino's value to a new valid value
    # INPUTS: N/A
    # OUTPUTS: N/A
    def randomize(self):
        self.value = random.randint(1, 6) + random.randint(1, 6) * 10

    # AUTHOR: Aarush Modi
    # DATE: April 3, 2021
    # PURPOSE: Draws Dots
    # INPUTS: Canvas, x, y
    # OUTPUTS: N/A
    def drawDots(self, x, y, canvas):
            canvas.create_oval(x + self.gap, y + self.gap, x + self.gap + self.diameter, y + self.gap + self.diameter,fill="black")
            canvas.create_oval(x + self.gap, y + self.gap, x + self.gap + self.diameter, y + self.gap + self.diameter,fill="black")

    # AUTHOR: Aarush Modi
    # DATE: April 3, 2021
    # PURPOSE: Creates domino
    # INPUTS: Canvas, x, y
    # OUTPUTS: N/A
    def draw(self, canvas, x, y):
        tensDigitValue = self.value// 10
        onesDigitValue = self.value % 10
        if self.orientation == "Horizontal":
            if tensDigitValue == 1:
                self.drawDots(x + (self.size * 0.3), y + (self.size * 0.3), canvas)
            elif tensDigitValue == 2:
                self.drawDots(x, y, canvas)
                self.drawDots(x + (self.size * 0.6), y + (self.size * 0.6), canvas)
            elif tensDigitValue == 3:
                self.drawDots(x, y, canvas)
                self.drawDots(x + (self.size * 0.3), y + (self.size * 0.3), canvas)
                self.drawDots(x + (self.size * 0.6), y + (self.size * 0.6), canvas)
            elif tensDigitValue == 4:
                self.drawDots(x, y, canvas)
                self.drawDots(x + (self.size * 0.6), y + (self.size * 0.6), canvas)
                self.drawDots(x, y + (self.size * 0.6), canvas)
                self.drawDots(x + (self.size * 0.6), y, canvas)
            elif tensDigitValue == 5:
                self.drawDots(x, y, canvas)
                self.drawDots(x + (self.size * 0.6), y + (self.size * 0.6), canvas)
                self.drawDots(x, y + (self.size * 0.6), canvas)
                self.drawDots(x + (self.size * 0.6), y, canvas)
                self.drawDots(x + (self.size * 0.3), y + (self.size * 0.3), canvas)
            else:
                self.drawDots(x, y, canvas)
                self.drawDots(x + (self.size * 0.6), y + (self.size * 0.6), canvas)
                self.drawDots(x, y + (self.size * 0.6), canvas)
                self.drawDots(x + (self.size * 0.6), y, canvas)
                self.drawDots(x, y + (self.size * 0.3), canvas)
                self.drawDots(x + (self.size * 0.6), y + (self.size * 0.3), canvas)
            if onesDigitValue == 1:
                self.drawDots(x + (self.size * 0.3) + self.size, y + (self.size * 0.3), canvas)
            elif onesDigitValue == 2:
                self.drawDots(x + self.size, y, canvas)
                self.drawDots(x + (self.size * 0.6) + self.size, y + (self.size * 0.6), canvas)
            elif onesDigitValue == 3:
                self.drawDots(x + self.size, y, canvas)
                self.drawDots(x + (self.size * 0.3) + self.size, y + (self.size * 0.3), canvas)
                self.drawDots(x + (self.size * 0.6) + self.size, y + (self.size * 0.6), canvas)
            elif onesDigitValue == 4:
                self.drawDots(x + self.size, y, canvas)
                self.drawDots(x + (self.size * 0.6) + self.size, y + (self.size * 0.6), canvas)
                self.drawDots(x + self.size, y + (self.size * 0.6), canvas)
                self.drawDots(x + (self.size * 0.6) + self.size, y, canvas)
            elif onesDigitValue == 5:
                self.drawDots(x + self.size, y, canvas)
                self.drawDots(x + (self.size * 0.6) + self.size, y + (self.size * 0.6), canvas)
                self.drawDots(x + self.size, y + (self.size * 0.6), canvas)
                self.drawDots(x + (self.size * 0.6) + self.size, y, canvas)
                self.drawDots(x + (self.size * 0.3) + self.size, y + (self.size * 0.3), canvas)
            else:
                self.drawDots(x + self.size, y, canvas)
                self.drawDots(x + (self.size * 0.6) + self.size, y + (self.size * 0.6), canvas)
                self.drawDots(x + self.size, y + (self.size * 0.6), canvas)
                self.drawDots(x + (self.size * 0.6) + self.size, y, canvas)
                self.drawDots(x + self.size, y + (self.size * 0.3), canvas)
                self.drawDots(x + (self.size * 0.6) + self.size, y + (self.size * 0.3), canvas)
        else:
            if tensDigitValue == 1:
                self.drawDots(x + (self.size * 0.3), y + (self.size * 0.3), canvas)
            elif tensDigitValue == 2:
                self.drawDots(x, y, canvas)
                self.drawDots(x + (self.size * 0.6), y + (self.size * 0.6), canvas)
            elif tensDigitValue == 3:
                self.drawDots(x, y, canvas)
                self.drawDots(x + (self.size * 0.3), y + (self.size * 0.3), canvas)
                self.drawDots(x + (self.size * 0.6), y + (self.size * 0.6), canvas)
            elif tensDigitValue == 4:
                self.drawDots(x, y, canvas)
                self.drawDots(x + (self.size * 0.6), y + (self.size * 0.6), canvas)
                self.drawDots(x, y + (self.size * 0.6), canvas)
                self.drawDots(x + (self.size * 0.6), y, canvas)
            elif tensDigitValue == 5:
                self.drawDots(x, y, canvas)
                self.drawDots(x + (self.size * 0.6), y + (self.size * 0.6), canvas)
                self.drawDots(x, y + (self.size * 0.6), canvas)
                self.drawDots(x + (self.size * 0.6), y, canvas)
                self.drawDots(x + (self.size * 0.3), y + (self.size * 0.3), canvas)
            else:
                self.drawDots(x, y, canvas)
                self.drawDots(x + (self.size * 0.6), y + (self.size * 0.6), canvas)
                self.drawDots(x, y + (self.size * 0.6), canvas)
                self.drawDots(x + (self.size * 0.6), y, canvas)
                self.drawDots(x, y + (self.size * 0.3), canvas)
                self.drawDots(x + (self.size * 0.6), y + (self.size * 0.3), canvas)
            if onesDigitValue == 1:
                self.drawDots(x + (self.size * 0.3) , y + (self.size * 0.3)+ self.size, canvas)
            elif onesDigitValue == 2:
                self.drawDots(x , y+ self.size, canvas)
                self.drawDots(x + (self.size * 0.6) , y + (self.size * 0.6)+ self.size, canvas)
            elif onesDigitValue == 3:
                self.drawDots(x , y+ self.size, canvas)
                self.drawDots(x + (self.size * 0.3) , y + (self.size * 0.3)+ self.size, canvas)
                self.drawDots(x + (self.size * 0.6) , y + (self.size * 0.6)+ self.size, canvas)
            elif onesDigitValue == 4:
                self.drawDots(x , y+ self.size, canvas)
                self.drawDots(x + (self.size * 0.6) , y + (self.size * 0.6)+ self.size, canvas)
                self.drawDots(x , y + (self.size * 0.6)+ self.size, canvas)
                self.drawDots(x + (self.size * 0.6) , y+ self.size, canvas)
            elif onesDigitValue == 5:
                self.drawDots(x , y+ self.size, canvas)
                self.drawDots(x + (self.size * 0.6) , y + (self.size * 0.6)+ self.size, canvas)
                self.drawDots(x , y + (self.size * 0.6)+ self.size, canvas)
                self.drawDots(x + (self.size * 0.6) , y+ self.size, canvas)
                self.drawDots(x + (self.size * 0.3) , y + (self.size * 0.3)+ self.size, canvas)
            else:
                self.drawDots(x , y+ self.size, canvas)
                self.drawDots(x + (self.size * 0.6) , y + (self.size * 0.6)+ self.size, canvas)
                self.drawDots(x , y + (self.size * 0.6)+ self.size, canvas)
                self.drawDots(x + (self.size * 0.6) , y+ self.size, canvas)
                self.drawDots(x , y + (self.size * 0.3)+ self.size, canvas)
                self.drawDots(x + (self.size * 0.6) , y + (self.size * 0.3)+ self.size, canvas)
def spaceKeyPress(key):
    if key.char == "s":
        domino1 = Domino()

        x = 50
        y = 50
        canvas.create_rectangle(x, y, x + domino1.size * 2, y + domino1.size, width=1, outline="black", fill="white")
        canvas.create_line(x+domino1.size, y , x +domino1.size, y + domino1.size)
        domino1.draw(canvas, x, y)
        x = 300
        y = 50
        domino1.flip()
        canvas.create_rectangle(x, y, x + domino1.size * 2, y + domino1.size, width=1, outline="black", fill="white")
        canvas.create_line(x + domino1.size, y, x + domino1.size, y + domino1.size)
        domino1.draw(canvas, x, y)
        x = 550
        y = 50
        domino1.flip()
        canvas.create_rectangle(x, y, x + domino1.size , y + domino1.size * 2, width=1, outline="black", fill="white")
        canvas.create_line(x, y+ domino1.size, x + domino1.size, y + domino1.size)
        domino1.setOrientation("Vertical")
        domino1.draw(canvas, x, y)
        x = 800
        y = 50
        canvas.create_rectangle(x, y, x + domino1.size * 2, y + domino1.size, width=1, outline="white", fill="red")
        canvas.create_line(x+domino1.size, y , x +domino1.size, y + domino1.size)
        domino1.setOrientation("Horizontal")
        domino1.draw(canvas, x, y)


#MAIN
domino = Tk()
domino.title = "Domino"

canvas = Canvas(domino, width=1000, height=900)
canvas.bind("<Key>", spaceKeyPress)
canvas.pack()
canvas.focus_set()





mainloop()
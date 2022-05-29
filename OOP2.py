# Author: Aarush Modi
# Date: April 29, 2021
# Purpose: Make a composition of classes for OOP2

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
            canvas.create_rectangle(x, y, x + self.size * 2,y + self.size, width=1, outline="black", fill="white")
            canvas.create_line(x+self.size, y , x +self.size, y + self.size)
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
#CLASS DOMINO END

# Author: Aarush Modi
# Date: April 29, 2021
# Purpose: Make a hand class for OOP2
# Data Elements: First Domino, Second Domino, Third Domino
# Methods:
# Initalize data elements (__init__)
# Return hand object value as string (__str__)
# Sets size of domino in a hand to a valid value(setSize)
# Orders the dominos (sort)
# Randomizes each of the three dominos in a hand (roll)
# Creates three dominos (draw)
# Determines largest run of a hand (getRun)
#Dependancies: Tkinter, Random, Domino class

class Hand:
    # AUTHOR: Aarush Modi
    # DATE: April 29, 2021
    # PURPOSE: Initalize data elements
    # INPUTS: Domino Class
    # OUTPUTS: N/A
    def __init__(self):
        self.firstDomino = Domino()
        self.secondDomino = Domino()
        self.thirdDomino = Domino()
        self.firstDomino.orientation = "Horizontal"
        self.secondDomino.orientation = "Horizontal"
        self.thirdDomino.orientation = "Horizontal"

    # AUTHOR: Aarush Modi
    # DATE: April 29, 2021
    # PURPOSE: Return hand object value as string
    # INPUTS: Domino Class
    # OUTPUTS: N/A
    def __str__(self):
        strHand = str(self.firstDomino.value) + " , " + str(self.secondDomino.value) + " , " + str(self.thirdDomino.value)
        return strHand

    #AUTHOR: Aarush Modi
    #DATE: April 29, 2021
    #PURPOSE: Sets size of domino in a hand to a valid value
    #INPUT: N/A
    #OUTPUT: N/A
    def setSize(self):
        self.firstDomino.getvalue() 
        self.secondDomino.getvalue() 
        self.thirdDomino.getvalue
        
    #AUTHOR: Aarush Modi
    #DATE: April 29, 2021
    #PURPOSE: Orders the dominos
    #INPUT: N/A
    #OUTPUT: N/A
    def sort(self):
##        if self.firstDomino.value > int(str(self.firstDomino.value[::-1])):
##            self.firstDomino.value = int(str(self.firstDomino.value[::-1]))
##        if self.secondDomino.value > int(str(self.secondDomino.value[::-1])):
##            self.secondDomino.value = int(str(self.secondDomino.value[::-1]))
##        if self.thirdDomino.value > int(str(self.thirdDomino.value[::-1])):
##            self.thirdDomino.value = int(str(self.thirdDomino.value[::-1]))
            
        small = min(self.firstDomino.value, self.secondDomino.value, self.thirdDomino.value)
        big = max(self.firstDomino.value, self.secondDomino.value, self.thirdDomino.value)
        mid = self.firstDomino.value + self.secondDomino.value + self.thirdDomino.value - small - big
        self.firstDomino.value = small
        self.secondDomino.value = mid
        self.thirdDomino.value = big

    #AUTHOR: Aarush Modi
    #DATE: April 29, 2021
    #PURPOSE: Randomizes each of the three dominos in a hand
    #INPUT: N/A
    #OUTPUT: N/A
    def roll(self):
        self.firstDomino.randomize() 
        self.secondDomino.randomize() 
        self.thirdDomino.randomize()
        
    #AUTHOR: Aarush Modi
    #DATE: April 29, 2021
    #PURPOSE: Creates three dominos
    #INPUT: N/A
    #OUTPUT: N/A
    def draw(self, canvas, x=0, y=0):
        self.firstDomino.draw(canvas, x = 10, y = 10)
        self.secondDomino.draw (canvas, x = 150, y=10)
        self.thirdDomino.draw (canvas, x= 300, y=10)
        
    #AUTHOR: Aarush Modi
    #DATE: April 29, 2021
    #PURPOSE: Determines largest run of a hand
    #INPUT: N/A
    #OUTPUT: N/A
    def getRun(self):
        onesDigitFirst = self.firstDomino.value % 10
        tensDigitFirst = self.firstDomino.value // 10
        onesDigitSecond = self.secondDomino.value % 10
        tensDigitSecond = self.secondDomino.value // 10
        onesDigitThird = self.thirdDomino.value % 10
        tensDigitThird = self.thirdDomino.value // 10
        ones = 0
        twos = 0
        threes = 0
        fours = 0
        fives = 0
        sixes = 0
        runs = 0
        if onesDigitFirst == 1:
            ones =+1
        elif onesDigitFirst == 2:
            twos =+ 1
        elif onesDigitFirst == 3:
            threes =+ 1
        elif onesDigitFirst == 4:
            fours =+ 1
        elif onesDigitFirst == 5:
            fives =+ 1
        elif onesDigitFirst == 6:
            sixes =+ 1
        if tensDigitFirst == 1:
            ones =+1
        elif tensDigitFirst == 2:
            twos =+ 1
        elif tensDigitFirst == 3:
            threes =+ 1
        elif tensDigitFirst == 4:
            fours =+ 1
        elif tensDigitFirst == 5:
            fives =+ 1
        elif tensDigitFirst == 6:
            sixes =+ 1
        if onesDigitSecond == 1:
            ones =+1
        elif onesDigitSecond == 2:
            twos =+ 1
        elif onesDigitSecond == 3:
            threes =+ 1
        elif onesDigitSecond == 4:
            fours =+ 1
        elif onesDigitSecond == 5:
            fives =+ 1
        elif onesDigitSecond == 6:
            sixes =+ 1
        if tensDigitSecond == 1:
            ones =+1
        elif tensDigitSecond == 2:
            twos =+ 1
        elif tensDigitSecond == 3:
            threes =+ 1
        elif tensDigitSecond == 4:
            fours =+ 1
        elif tensDigitSecond == 5:
            fives =+ 1
        elif tensDigitSecond == 6:
            sixes =+ 1
        if onesDigitThird == 1:
            ones =+1
        elif onesDigitThird == 2:
            twos =+ 1
        elif onesDigitThird == 3:
            threes =+ 1
        elif onesDigitThird == 4:
            fours =+ 1
        elif onesDigitThird == 5:
            fives =+ 1
        elif onesDigitThird == 6:
            sixes =+ 1
        if tensDigitThird== 1:
            ones =+1
        elif tensDigitThird == 2:
            twos =+ 1
        elif tensDigitThird == 3:
            threes =+ 1
        elif tensDigitThird == 4:
            fours =+ 1
        elif tensDigitThird == 5:
            fives =+ 1
        elif tensDigitThird == 6:
            sixes =+ 1
        if tensDigitFirst == onesDigitFirst:
            if tensDigitFirst == 1 and ones != 4:
                ones = ones - 1
            elif tensDigitFirst == 2 and twos != 4:
                twos = twos - 1
            elif tensDigitFirst == 3 and threes != 4:
                threes = threes - 1
            elif tensDigitFirst == 4 and fours != 4:
                fours = fours - 1
            elif tensDigitFirst == 5 and fives != 4:
                fives = fives - 1
            elif tensDigitFirst == 6 and sixes != 4:
                sixes = sixes - 1
        if tensDigitSecond == onesDigitSecond:
            if tensDigitSecond == 1 and ones != 4:
                ones = ones - 1
            elif tensDigitSecond == 2 and twos != 4:
                twos = twos - 1
            elif tensDigitSecond == 3 and threes != 4:
                threes = threes - 1
            elif tensDigitSecond == 4 and fours != 4:
                fours = fours - 1
            elif tensDigitSecond == 5 and fives != 4:
                fives = fives - 1
            elif tensDigitSecond == 6 and sixes != 4:
                sixes = sixes - 1
        if tensDigitThird == onesDigitThird:
            if tensDigitThird == 1 and ones != 4:
                ones = ones - 1
            elif tensDigitThird == 2 and twos != 4:
                twos = twos - 1
            elif tensDigitThird == 3 and threes != 4:
                threes = threes - 1
            elif tensDigitThird == 4 and fours != 4:
                fours = fours - 1
            elif tensDigitThird == 5 and fives != 4:
                fives = fives - 1
            elif tensDigitThird == 6 and sixes != 4:
                sixes = sixes - 1
        if ones == 2 or ones == 3:
            runs = 2 
            if twos == 2 or twos == 3:
                runs += 1
            elif threes == 2 or threes == 3:
                runs += 1
            elif fours == 2 or fours == 3:
                runs += 1
            elif fives == 2 or fives == 3:
                runs += 1
            elif sixes == 2 or sixes == 3:
                runs += 1
        elif twos == 2 or twos == 3:
            runs = 2
            if ones == 2 or ones == 3:
                runs += 1
            elif threes == 2 or threes == 3:
                runs += 1
            elif fours == 2 or fours == 3:
                runs += 1
            elif fives == 2 or fives == 3:
                runs += 1
            elif sixes == 2 or sixes == 3:
                runs += 1
        elif threes == 2 or threes == 3:
            runs = 2
            if twos == 2 or twos == 3:
                runs += 1
            elif ones == 2 or ones == 3:
                runs += 1
            elif fours == 2 or fours == 3:
                runs += 1
            elif fives == 2 or fives == 3:
                runs += 1
            elif sixes == 2 or sixes == 3:
                runs += 1
        elif fours == 2 or fours == 3:
            runs = 2
            if twos == 2 or twos == 3:
                runs += 1
            elif threes == 2 or threes == 3:
                runs += 1
            elif ones == 2 or ones == 3:
                runs += 1
            elif fives == 2 or fives == 3:
                runs += 1
            elif sixes == 2 or sixes == 3:
                runs += 1
        elif fives == 2 or fives == 3:
            runs = 2
            if twos == 2 or twos == 3:
                runs += 1
            elif threes == 2 or threes == 3:
                runs += 1
            elif fours == 2 or fours == 3:
                runs += 1
            elif ones == 2 or ones == 3:
                runs += 1
            elif sixes == 2 or sixes == 3:
                runs += 1
        elif sixes == 2 or sixes == 3:
            runs = 2
            if twos == 2 or twos == 3:
                runs += 1
            elif threes == 2 or threes == 3:
                runs += 1
            elif fours == 2 or fours == 3:
                runs += 1
            elif fives == 2 or fives == 3:
                runs += 1
            elif ones == 2 or ones == 3:
                runs += 1
        elif ones == 4 or ones == 6 or twos == 4 or twos == 6 or threes == 4 or threes == 6 or fours == 4 or fours == 6 or fives == 4 or fives == 6 or sixes == 4 or sixes == 6:
            runs = 3
        
        if self.firstDomino.value == self.secondDomino.value or self.firstDomino.value == self.thirdDomino.value or self.thirdDomino.value == self.secondDomino.value:
            runs = 2
            
        if self.firstDomino.value == self.secondDomino.value and self.firstDomino.value == self.thirdDomino.value:
            runs = 3
        return runs
    
    #AUTHOR: Aarush Modi
    #DATE: April 29, 2021
    #PURPOSE: Keypressed Event
    #INPUT: N/A
    #OUTPUT: N/A
    def keyPressDown(keyDown, key):
        if key.char == "t" or key.char == "T":
            runs = 0
            runs0 = 0
            runs2 = 0
            runs3 = 0
            count = 0
            while count < 10000:
                DominoY = Hand()
                DominoY.roll()
                runs = DominoY.getRun()
                if runs == 0:
                    runs0 +=1
                elif runs == 2:
                    runs2 += 1
                elif runs == 3:
                    runs0 += 1
                count +=1
            runs = runs0 + runs2 + runs3
            print ("1000 Random Dominoes Were Created")
            print ("The statistics are: ")
            print ("Total number of runs: ", runs)
            print ("    Runs of 0: ", runs0/10000 * 100, "%")
            print ("    Runs of 2: ", runs2/10000 * 100, "%")
            print ("    Runs of 3: ", runs3/10000 * 100, "%")
            print ("    Percentage of runs: ", runs/10000 * 100, "%")
        elif key.char == "r" or key.char == "R":
            x= 15
            y= 15
            DominoX = Hand()
            DominoX.roll()
            DominoX.sort()
            DominoX.draw(canvas, x, y)
            runs = DominoX.getRun()
            print ("There are: ", runs, " runs")
#MAIN

root = Tk()
root.title = ("Dominoes")                 
canvas = Canvas(root, width=475, height = 100)
canvas.config(background = "white")
handObject = Domino()
canvas.pack()
canvas.focus_set()

handObject2 = Domino()
value1 = handObject.value
value2 = handObject2.value
add = value1 + value2
sub = value1 - value2
mul = value1 * value2
print ("The sum is: ", add)
print ("The diffrence is: ", sub)
print ("The product is: ", mul)

if value1 > value2:
    print("First domino is greater than second domino: True")
else:
    print("First domino is greater than second domino: False")
if value1 >= value2:
    print("First domino is greater than or equal to second domino: True")
else:
    print("First domino is greater than or equal to domino date: False")
if value1 < value2:
    print("First domino is less than second domino: True")
else:
   print("First domino is less than second domino: False")
if value1 <= value2:
    print("First domino is less than or equal to second domino: True")
else:
    print("First domino is less than or equal to second domino: False")
if value1 == value2:
    print("First domino is equal to second domino: True")
else:
    print("First domino is equal to second domino: False")
if value1 != value2:
    print("First domino is not equal to second domino: True")
else:
    print("First domino is not equal to second domino: False")
mainloop()













            

    

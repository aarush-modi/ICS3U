#Author: Aarush Modi
#Date: March 22, 2021
#Purpose: To play around with numbers
import random
from tkinter import*

NumberTheory = Tk()

userInput1 = IntVar()
userInput1.set(value = "1")
userInput2 = IntVar()
userInput2.set(value = "1")

#userInput1 = int(userInput1)
#userInput2 = int (userInput2)

permutationAnswer = StringVar()
permutationAnswer.set(value = "Enter Two Positive Integers and Click 'Calculate Number Theory'")
combinationAnswer = StringVar()
combinationAnswer.set(value = "Find The Number of Combinations")
lcmAnswer = StringVar()
lcmAnswer.set(value = "Find the Lowest Common Multiple")
gcdAnswer = StringVar()
gcdAnswer.set(value = "Find the Greatest Common Denominator")
relitivelyPrimeAnswer = StringVar()
relitivelyPrimeAnswer.set(value = "Find if the Numbers Are Relitively Prime")

#Author: Aarush Modi
#Date: March 13, 2021
#Purpose: To calculate the factorial of a given number
#Input: Two numbers
#Output: Factorial
def calcFactorial (number):
    if number == 0:
        factorial = 1
    else:
        count = 1
        factorial = 1
        while count < (number + 2):
            factorial = factorial * count
            count += 1
    return factorial

#Author: Aarush Modi
#Date: March 13, 2021
#Purpose: To calculate GCD of two given numbers
#Input: Two numbers
#Output: GCD
def calcGCD (userInput1, userInput2):
    t = userInput1 % userInput2
    while t != 0:
        userInput1 = userInput2
        userInput2 = t
        t = userInput1 % userInput2
    return userInput2

#Author: Aarush Modi
#Date: March 13, 2021
#Purpose: To calculate number of permutations of two given numbers
#Input: Two numbers
#Output: Permutations
def calcPermutations (intUserInput1, userInput2):
    if userInput2 > intUserInput1:
        thirdNumber = intUserInput1
        intUserInput1 = userInput2
        userInput2 = thirdNumber
    permutation = calcFactorial(intUserInput1)/calcFactorial(intUserInput1 - userInput2)
    return permutation

#Author: Aarush Modi
#Date: March 13, 2021
#Purpose: To calculate the number of combinations of two given numbers
#Input: Two numbers
#Output: Combinations
def calcCombinations (userInput1, userInput2):
        if userInput2 > userInput1:
            thirdNumber = userInput1
            userInput1 = userInput2
            userInput2 = thirdNumber
        combination = calcFactorial(userInput1)/(calcFactorial(userInput2) * calcFactorial(userInput1-userInput2))
        return combination

#Author: Aarush Modi
#Date: March 13, 2021
#Purpose: To calculate LCM of two given numbers
#Input: Two numbers
#Output: LCM
def calcLCM (userInput1, userInput2):
    LCM = (userInput1 * userInput2)/(calcGCD(userInput1, userInput2))
    return LCM

#Author: Aarush Modi
#Date: March 13, 2021
#Purpose: To calculate wether two numbers are relitively prime
#Input: Two numbers
#Output: True or False
def isRelativelyPrime (intUserInput1, userInput2):
    if calcGCD(intUserInput1, userInput2) == 1:
        return True
    else:
        return False


#Author: Aarush Modi
#Date: March 24, 2021
#Purpose: To preform Number Theory
#Input: N/A
#Output: Number Theory
def calcButtonPressed(userInput1,userInput2):

    if (type(userInput1) != int or userInput1 <= 0):
        userInput1 = 1
        permutationAnswer.set(value = "Your First Number is Not a Positive Integer")
    if (type(userInput2) != int or userInput2 <= 0):
        userInput2 = 1
        permutationAnswer.set(value = "Your Second Number is Not a Positive Integer")

    thirdNumber = min(userInput1,userInput2)
    userInput2 = max(userInput1,userInput2)
    userInput1 = thirdNumber

    outputPermutation = (calcPermutations(userInput1, userInput2))
    outputPermutation = str(outputPermutation)
    outputCombination = (calcCombinations(userInput1, userInput2))
    outputCombination = str(outputCombination)
    outputLCM = (calcLCM(userInput1, userInput2))
    outputLCM = str(outputLCM)
    outputGCD = (calcGCD(userInput1, userInput2))
    outputGCD = str(outputGCD)
    outputPrime = (isRelativelyPrime(userInput1, userInput2))

    combinationAnswer.set(value="There are " + outputCombination + " Combinations")
    permutationAnswer.set(value="There are " + outputPermutation + " Permutations")
    lcmAnswer.set(value="The Lowest Common Multiple is: " + outputLCM)
    gcdAnswer.set(value="The Greatest Common Denominator is: " + outputGCD)
    if outputPrime == True:
        relitivelyPrimeAnswer.set(value="The Numbers Are Relitively Prime")
    else:
        relitivelyPrimeAnswer.set(value="The Numbers Are Not Relitively Prime")
#MAIN


input1 = Label (NumberTheory, text="Enter Positive Integer: ", height = 2)
input1.grid (row = 0, column = 0, sticky = W, padx = 10, pady = 5)
input2 = Label (NumberTheory, text="Enter Positive Integer: ", height = 2)
input2.grid (row = 1, column = 0, sticky = W, padx = 10, pady = 5)

intUserInput1 = Entry(NumberTheory, width = 8, textvariable = userInput1)
intUserInput1.grid(row=0, column = 1, padx = 10, pady = 5)
userInput2 = Entry(NumberTheory, width = 8, textvariable = userInput2)
userInput2.grid(row=1, column = 1, padx = 10, pady = 5)

buttonCalc = Button(NumberTheory, text = "Calculate Number Theory", width = 24,height = 2,command = lambda:calcButtonPressed(userInput1.get(),userInput2.get()))
buttonCalc.grid(row = 2, column = 0, columnspan = 2, rowspan = 3, padx = 10, pady = 5)

permutations = Label (NumberTheory, textvariable = permutationAnswer, width = 48)
permutations.grid (row = 0, column = 3, sticky = W, padx = 10, pady = 5)
combinations = Label (NumberTheory, textvariable = combinationAnswer, width = 48)
combinations.grid (row = 1, column = 3, sticky = W, padx = 10, pady = 5)
lcm =  Label (NumberTheory, textvariable = lcmAnswer, width = 48)
lcm.grid (row = 2, column = 3, sticky = W, padx = 10, pady = 5)
gcd =  Label (NumberTheory, textvariable = gcdAnswer, width = 48)
gcd.grid (row = 3, column = 3, sticky = W, padx = 10, pady = 5)
relitivelyPrime =  Label (NumberTheory, textvariable = relitivelyPrimeAnswer, width = 48)
relitivelyPrime.grid (row = 4, column = 3, sticky = W, padx = 10, pady = 5)


mainloop()

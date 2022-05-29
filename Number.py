#Author: Aarush Modi
#Date: March 13, 2021
#Purpose: To understand Functions in PY3
import random

#Author: Aarush Modi
#Date: March 13, 2021
#Purpose: To get a random number in between two positive integers
#Input: Two numbers
#Output: Random Number
def getPositiveInteger (lowNumber, highNumber):
    if ((lowNumber > 0) and (highNumber >0) and (type(lowNumber) == int) and (type(highNumber) == int)and (lowNumber<highNumber)):
        rndNumber = random.randrange(lowNumber,highNumber)
        #Output
        return rndNumber
    else:
        #Output
        print ("Please input low positive integer followed by a high positive integer.")

#Author: Aarush Modi
#Date: March 13, 2021
#Purpose: To calculate the factorial of a given number
#Input: Two numbers
#Output: Factorial
def calcFactorial (number):
    if number == 0:
        return 1
    else:
        return number * calcFactorial(number-1)
#Author: Aarush Modi
#Date: March 13, 2021
#Purpose: To calculate GCD of two given numbers
#Input: Two numbers
#Output: GCD
def calcGCD (firstNumber, secondNumber):
    mark = (firstNumber % secondNumber)
    while (not mark == 0):
        firstNumber = secondNumber
        secondNumber = mark
        mark = (firstNumber % secondNumber)
    return secondNumber
#Author: Aarush Modi
#Date: March 13, 2021
#Purpose: To calculate number of permutations of two given numbers
#Input: Two numbers
#Output: Permutations
def calcPermutations (firstNumber, secondNumber):
    if secondNumber > firstNumber:
        thirdNumber = firstNumber
        firstNumber = secondNumber
        secondNumber = thirdNumber
    permutation = calcFactorial(firstNumber)/calcFactorial(firstNumber - secondNumber)
    return permutation

#Author: Aarush Modi
#Date: March 13, 2021
#Purpose: To calculate the number of combinations of two given numbers
#Input: Two numbers
#Output: Combinations
def calcCombinations (firstNumber, secondNumber):
        if secondNumber > firstNumber:
            thirdNumber = firstNumber
            firstNumber = secondNumber
            secondNumber = thirdNumber
        combination = calcFactorial(firstNumber)/(calcFactorial(secondNumber) * calcFactorial(firstNumber-secondNumber))
        return combination

#Author: Aarush Modi
#Date: March 13, 2021
#Purpose: To calculate LCM of two given numbers
#Input: Two numbers
#Output: LCM
def calcLCM (firstNumber, secondNumber):
    LCM = (firstNumber * secondNumber)/calcGCD(firstNumber, secondNumber)
    return LCM

#Author: Aarush Modi
#Date: March 13, 2021
#Purpose: To calculate wether two numbers are relitively prime
#Input: Two numbers
#Output: True or False
def isRelativelyPrime (firstNumber, secondNumber):
    if calcGCD(firstNumber, secondNumber) == 1:
        return True
    else:
        return False

#MAIN PROGRAM
while True:
    lowNumber = int(input("Enter low positive integer: "))
    highNumber= int(input("Enter high positive integer: "))
    if((type(highNumber) == int) and (type(lowNumber) == int) and (lowNumber<highNumber) and (lowNumber > 0) and (highNumber >0)):
        getPositiveInteger(lowNumber,highNumber)
        print("Number of Permutations: ",calcPermutations(lowNumber,highNumber))
        print("Number of Combinations: ",calcCombinations (lowNumber,highNumber))
        print ("Lowest Common Multiple: ",calcLCM(lowNumber,highNumber))
        print("Createst Common Denominator: ",calcGCD(lowNumber,highNumber))
        print("Relitively Prime: ",isRelativelyPrime(lowNumber,highNumber))
    else:
        print ("Please input low positive integer followed by a high positive integer.")
    continue















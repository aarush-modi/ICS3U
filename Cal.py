 #Author: Aarush Modi
#Date: March 29, 2021
#Purpose: To create a Calender Class for OOP1

#Author: Aarush Modi
# DATE: 3/29/2021
# PURPOSE: Class for calender
# DATA ELEMENTS: input day(intDay), input month(intMonth), input year(intYear)
# MEHTODS:
# Initialize data elements(__init__)
# Return the name of a month(returnMonth)
# Return if the year is leap(returnleapYear)
# Returns the maximum number of days in a month(returnMaxDay)
# Calculate the day of first date of the month(calcZeller)
# Return the  name of the day(returnDayName)
# Returns if the day is real or not(calcValid)
# Gets and confirms date(getDate)
# Converts date to string(__str__),
# Displays the calender(displayCalender)

class Date:

    # AUTHOR: Jerry Liu
    # DATE: 3/29/2021
    # PURPOSE: Initialize the data elements
    # input: N/A
    # output: N/A
    def __init__(self):
        self.intDay = 1
        self.intMonth = 1
        self.intYear = 2019
        if self.intDay < 1 or self.intDay > self.returnMaxDay():
            self.intDay = 1
            self.intMonth = 1
            self.intYear = 2019
        elif self.intMonth < 1 or self.intMonth > 12:
            self.intDay = 1
            self.intMonth = 1
            self.intYear = 2019
        elif self.intYear < 1600 or self.intYear > 2200:
            self.intDay = 1
            self.intMonth = 1
            self.intYear = 2019

    # AUTHOR: Aarush Modi
    # DATE: 3/29/2021
    # PURPOSE: Return the name of a month
    # input: N/A
    # output: Month in string
    def returnMonth(self):
        if self.intMonth == 1:
           strMonth = "January"
        elif self.intMonth == 2:
           strMonth = "February"
        elif self.intMonth == 3:
           strMonth = "March"
        elif self.intMonth == 4:
           strMonth = "April"
        elif self.intMonth == 5:
           strMonth = "May"
        elif self.intMonth == 6:
           strMonth = "June"
        elif self.intMonth == 7:
           strMonth = "July"
        elif self.intMonth == 8:
           strMonth = "August"
        elif self.intMonth == 9:
           strMonth = "September"
        elif self.intMonth == 10:
           strMonth = "October"
        elif self.intMonth == 11:
           strMonth = "November"
        else:
           strMonth = "December"
        return strMonth

    # AUTHOR: Aarush Modi
    # DATE: 3/29/2021
    # PURPOSE: Return if the year is leap
    # input: N/A
    # output: T or F
    def returnLeapYear(self):
        if self.intYear % 100 == 0:
            if self.intYear % 400 == 0:
                leapYear = True
            else:
                leapYear = False
        elif self.intYear % 4 == 0:
            leapYear = True
        else:
            leapYear = False
        return leapYear

    # AUTHOR: Aarush Modi
    # DATE: 3/29/2021
    # PURPOSE: Returns the maximum number of days in a month
    # input: N/A
    # output: Maximum days in a month
    def returnMaxDay(self):
        if self.intMonth == 1 or self.intMonth == 3 or self.intMonth == 5 or self.intMonth == 7 or self.intMonth == 8 or self.intMonth == 10 or self.intMonth == 12:
            maxDay = 31
        elif self.intMonth == 2:
            maxDay = 28
            if self.returnLeapYear() == True:
                maxDay = 29
        else:
            maxDay = 30
        return maxDay

    # AUTHOR: Aarush Modi
    # DATE: 3/29/2021
    # PURPOSE: Calculate the day of first date of the month
    # Input: N/A
    # Output: Integers between 0-6
    def calcZeller(self):
        m = self.intMonth - 2
        y = self.intYear
        if m <= 0:
            m = m + 12
            y = y - 1
        p = y // 100
        r = y % 100
        return (self.intDay + (26 * m - 2) // 10 + r + r // 4 + p // 4 + 5 * p) % 7

    # AUTHOR: Aarush Modi
    # DATE: 3/29/2021
    # PURPOSE: Return the  name of the day
    # input: N/A
    # output: String day name
    def returnDayName(self):
        if self.calcZeller() == 0:
            dayName = "Sunday"
        elif self.calcZeller() == 1:
            dayName = "Monday"
        elif self.calcZeller() == 2:
            dayName = "Tuesday"
        elif self.calcZeller() == 3:
            dayName = "Wednesday"
        elif self.calcZeller() == 4:
            dayName = "Thursday"
        elif self.calcZeller() == 5:
            dayName = "Friday"
        elif self.calcZeller() == 6:
            dayName = "Saturday"
        return dayName

    # AUTHOR: Aarush Modi
    # DATE: 3/29/2021
    # PURPOSE: Returns if the day is real or not
    # input: N/A
    # output: T or F
    def calcValid(self):
        if self.intDay < 1 or self.intDay > self.returnMaxDay():
            valid = False
        elif self.intMonth < 1 or self.intMonth > 12:
            valid = False
        elif self.intYear < 1600 or self.intYear > 2200:
            valid = False
        else:
            valid = True
        return valid

    # AUTHOR: Aarush Modi
    # DATE: 3/31/2021
    # PURPOSE: Gets and confirms date
    # input: Date
    # output: N/A
    def getDate(self):
        self.intDay = input("Please enter the day (1- 31): ")
        while self.intDay.isdigit() == False:
            self.intDay = input("Please enter the day (1- 31): ")
        self.intDay = int(self.intDay)

        self.intMonth = input("Please enter the month between 1 and 12: ")
        while self.intMonth.isdigit() == False:
            self.intMonth = input("Please enter the month between 1 and 12: ")
        self.intMonth = int(self.intMonth)

        self.intYear = input("Please enter the year between 1600 and 2200: ")
        while self.intYear.isdigit() == False:
            self.intYear = input("Please enter the year between 1600 and 2200: ")
        self.intYear = int(self.intYear)

    # AUTHOR: Aarush Modi
    # DATE: 3/31/2021
    # PURPOSE: Converts date to string
    # input: N/A
    # output: Date as string
    def __str__(self):
        strDate = self.returnDayName() + ", " + self.returnMonth() + " " + str(self.intDay) + ", " + str(self.intYear)
        return strDate

# AUTHOR: Aarush Modi
    # DATE: 3/31/2021
    # PURPOSE: Displays the calender
    # input: N/A
    # output: Calender
    def displayCalender(self):

        self.intDay = 1
        day = self.calcZeller() - 1

        space = ''
        space = space.rjust(3, ' ')

        print("        ", self.returnMonth(), self.intYear)
        print(' S ', ' M ', ' T ', ' W ', ' T ', ' F ', ' S ')

        if self.intMonth == 9 or self.intMonth == 4 or self.intMonth == 6 or self.intMonth == 11:
            for i in range(31 + day):
                if i <= day:
                    print(space, end=' ')
                else:
                    print("{:02d}".format(i - day), end='  ')
                    if (i + 1) % 7 == 0:
                        print()
        elif self.intMonth == 2:
            if self.intYear % 4 == 0:
                p = 30
            else:
                p = 29

            for i in range(p + day):
                if i <= day:
                    print(space, end=' ')
                else:
                    print("{:02d}".format(i - day), end='  ')
                    if (i + 1) % 7 == 0:
                        print()
        else:
            for i in range(32 + day):
                if i <= day:
                    print(space, end=' ')
                else:
                    print("{:02d}".format(i - day), end='  ')
                    if (i + 1) % 7 == 0:
                        print()

#MAIN

flag = "Again"
while flag == "Again":
    calender = Date()
    calender.getDate()
    while not(calender.calcValid):
        calender.getDate()
    print()
    print(calender)
    print()
    calender.displayCalender()
    print()
    flag = input("If you would like to repeat the process type 'Again', otherwise type 'No'")
    while not (flag == "Again" or flag == "No"):
        flag = input("If you would like to repeat the process type 'Again', otherwise type 'No'")

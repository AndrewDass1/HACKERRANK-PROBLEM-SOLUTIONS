# Context
An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.<br>
<br>
In the Gregorian calendar, three conditions are used to identify leap years:<br>
<br>
    The year can be evenly divided by 4, is a leap year, unless: <br>
        The year can be evenly divided by 100, it is NOT a leap year, unless: <br>
            The year is also evenly divisible by 400. Then it is a leap year. <br>

This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. <br>

# Task
Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False. <br>
<br>
Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function. 

# Procedure
From the Context and Task instructions, any year is to be inputted through a function and tell whether it is a leap year or not. <br>
Once again a leap year is: <br>
A year divisible by 4 but not 100 unless the number is divisible by 100 and 400 <br>

Example leap years: <br>
4 <br>
8 <br>
64 <br>
128 <br>
400 <br>
800 <br>
These numbers are either divisible by 4 or both 4 and 400. If a number is divisible by 400, it always divisible by 100. <br>

Example not leap years: <br>
100 <br>
200 <br>
300 <br>
500 <br>
These numbers are divisible by 4 but also divisible by 100, therefore they are not leap years. <br>
<br>
By knowing this information, an if-elif block can be used to iterate through the leap year conditions to validify which number is a leap year. <br>
<br>
Remember an if statement is executed and returns a True statement, the if-elif block finishes running and returns True. Organzing the structure of each if statement is crucial<br>
to make sure each condition is went through to prove any number is either a leap or not a leap year. 

# Solution
```
def is_leap(year):
    leap = False
    
    # Write your logic here
    if (year % 400 == 0):
        return True
    elif (year % 100 == 0):
        return False
    elif (year % 4 == 0):
        return True
    else:
        return False
    
    return leap
```

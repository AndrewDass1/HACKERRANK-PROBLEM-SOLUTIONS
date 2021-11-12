# Task

Given an integer, n perform the following conditional actions: <br>
    If n is odd, print Weird <br>
    If n is even and in the inclusive range of 2 to 5, print Not Weird <br >
    If n is even and in the inclusive range of 6 to 20, print Weird <br>
    If n is even and greater than 20, print Not Weird <br>

# Procedure
1. Declare variable n as an integer
```
n = int(input(""))
```

2. Create a if and else block to go through the conditions the task specified. <br>
Keep track of which conditions were declared and iterate through all of them. <br>
<br>

```
if n % 2 == 0 and n >=2 and n<=5:
    print('Not Weird')
elif n % 2 == 0 and n >=6 and n<=20:
    print('Weird')
elif n % 2 == 0 and n > 20:
    print('Not Weird')
else:
    print('Weird')
```
To explain the code above, the task specified to satisfy four conditions. Three of those conditions allows the number to be even and while only one of the conditions specified only allowed the number to be odd.<br>
<br>
A way to compete this code is to make many if-elif statements to check whether the inputted number n is even otherwise if it is not even, then the else statement will output a statement to show the number is not even. 

# Solution
```
n = int(input(""))

if n % 2 == 0 and n >=2 and n<=5:
    print('Not Weird')
elif n % 2 == 0 and n >=6 and n<=20:
    print('Weird')
elif n % 2 == 0 and n > 20:
    print('Not Weird')
else:
    print('Weird')
```

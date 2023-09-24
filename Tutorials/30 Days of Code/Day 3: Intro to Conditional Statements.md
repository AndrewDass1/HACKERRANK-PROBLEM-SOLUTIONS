# Intro to Conditional Statements
## Task
Given an integer, n, perform the following conditional actions: <br>
<br>
If n is odd, print 'Weird' <br>
If n is even and in the inclusive range of 2 to 5, print 'Not Weird' <br>
If n is even and in the inclusive range of 6 to 20, print 'Weird' <br>
If n is even and greater than 20, print 'Not Weird' <br> <br>

Link to the problem: https://www.hackerrank.com/challenges/30-conditional-statements/problem
## Explanation
To print certain statements, an if-and-else conditional block can be implemented to check if one or more statements are satisfied, it will print what was written in the certain if or else statement block. <br>
<br>
Below shows how to write an if statement:
```
if "check_condition" operation "to_next_condition":
  # Indent with Tab or four spaces, then write statement here
```
After an if statement, an else statement can be added:
```
if "check_condition" operation "to_next_condition": 
  # Indent with Tab or four spaces, then write statement here
else:
  # Indent with Tab or four spaces, then write statement here
```
To add more statements, elif can be specified after if and before else. elif means else if, which successfully executes an else statement to be another if statement. <br> <br> 

Within the conditional block, 'if' isn't executed, then the block will search to see if an 'elif' statement is true to be executed. If none of the 'elif' statements are true, then the 'else' statement will be executed. There can only be one if and else statement in the conditional block, and they must be the first and last statements respectively. No condition is written with else. There is no limit to how many 'elif' statements can be specified. <br> <br>

To check if a number is odd, the modulus operator '%' can be used. Using division with modulus returns the remainder instead of how many times a number goes into another number. If a modulus division operation is not zero, it is odd. If a modulus division operation is zero, then it is even. For one statement to check for more than one condition, the keyword "and" can be used to check if every condition is true. "or" can also be used but it prints the statement if only one condition is true among every other condition to check. <br> <br>

Below shows four statements using if, elif, elif, elif, and else with the keyword 'and" to check if one of the five conditional statements is true:
```
if __name__ == '__main__':
    N = int(input().strip())
    if N%2 != 0:
        print("Weird")
    elif N%2 == 0 and N >=2 and N <=5:
        print("Not Weird")
    elif N%2 == 0 and N >=6 and N <=20:
        print("Weird")
    elif N%2 == 0 and N>20:
        print("Not Weird")
    else:
        pass
```

## Solution
```
#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input().strip())
    if N%2 != 0:
        print("Weird")
    elif N%2 == 0 and N >=2 and N <=5:
        print("Not Weird")
    elif N%2 == 0 and N >=6 and N <=20:
        print("Weird")
    elif N%2 == 0 and N>20:
        print("Not Weird")
    else:
        pass
```

# Day 5: Loops
## Task
Given an integer, n, print its first 10 multiples. Each multiple n x i (where 1 <= i <= 10) should be printed on a new line in the form: n x i = result. <br>
## Example
n = 3 <br>
The printout should look like this:
```
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30
```
Link to the problem: https://www.hackerrank.com/challenges/30-loops/problem

## Explanation
A predefined variable called n is an integer data type that is declared to be used find is first 10 multiples. By using a for loop, its first 10 multiples can be calcuated. As stated in the "Example" directions, the final solution requires the output to be formatted such as:
```
numeric_value_of_n x current_iteration_of_multiple = result
```
The statement above is a string, therefore, the numeric values must be calcuated first and then casted to a string to be written into the format as shown above. When the script runs, it asks for a value for n once, therefore, another variable can be declared that can cast it into a string.
```
#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    str_n = str(n)
```
Afterwards, a for loop can be created to iterate through one to 10 and calcuate multiplying n by the current iteration. 

## Solution
```
if __name__ == '__main__':
    n = int(input().strip())
    str_n = str(n)
    for i in range(1, 11):
        statement = str_n + ' x ' + str(i) + ' ='
        result = n * i
        print(statement, result)
```
In a for loop, the last iteration that is always executed is the ending number - 1. Since 11 is the end for the iteration, it will execute the number before it as the last iteration, which will be 10. <br>
In the for loop, the 'statement' variable is declared to write out the format: 
```
numeric_value_of_n x current_iteration = 
```
Afterward, the 'result' variable calculates the multiplication for n and the current iteration and then the value is added to the string statement when it is printed to the console. Using one or more ',' in a print statement can be used to print more than one variable or string by only using one print statement. The ',' also automatically separates each variable or string with a space.

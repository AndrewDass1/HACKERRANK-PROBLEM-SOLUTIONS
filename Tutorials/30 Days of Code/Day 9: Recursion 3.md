# Day 9: Recursion 3
## Task
Complete the factorial function in the editor below. Be sure to use recursion. <br>
<br>
Factorial has the following parameter: <br>
* int n: an integer returns int: the factorial of n <br>
<br>
Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of 0.
<br> <br>
Link to the problem: https://www.hackerrank.com/challenges/30-recursion/problem

## Explanation
When a number is inputted, that number is multiplied by every number that is below it in value except for 0 and negative numbers. For example, if the number 3 is inputted, then the factorial of 3 is multiplying 3 by 2 by 1, which would give 6. <br> 
<br>

If n is either 1 or 2, then the factorial would be 1 or 2 respectively, therefore in both these scenarios the value of n can be immediately returned. <br>
<br>

For any number greater or equal to 3, then a multiplication counter equal to 1 and a for-loop can be declared. The for loop iterates from 1 to specifed n + 1. A for loop always stops at the nunber before the specified number, which is why the +1 is necessary to loop to the specified number n. In the for-loop, the variable equal to 1 is being multiplied by every iteration of i, to multiply every number until it reaches n. An if-else statement was implemented for all three scenarios.   


## Solution
```
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def factorial(n):
    if n == 1:
        return n
    elif n == 2:
        return n
    else:
        mult_result = 1
        for i in range(1, n + 1):
            mult_result *= i
        
        n = mult_result
        return n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
```

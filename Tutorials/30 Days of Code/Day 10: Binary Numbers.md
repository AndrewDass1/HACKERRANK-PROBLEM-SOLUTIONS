# Day 10: Binary Numbers

## Task
Given a base-10 integer, n, convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation. When working with different bases, it is common to show the base as a subscript. <br>
<br>
Link to the problem: https://www.hackerrank.com/challenges/30-binary-numbers/problem

## Explanation
### How to Convert Decimal to Binary
In this problem, a decimal number is given by default and must be converted to binary. To convert any decimal number to binary the procedure is:
1. Take the decimal number and divide by 2. This example will use 6 as the decimal number
```
6 / 2 = 3 R 0
```
After every division, keep note of each remainder number. The division process continues until the result is 0. 
```
6 / 2 = 3 R 0
3 / 2 = 1 R 1
1 / 2 = 0 R 1 - Last division, since the result is 0. 
```
2. Arrange the remainder values from bottom to top to left to right will be the number in binary. In this case, the 6's decimal equivalent is 100 in binary. 

### How to Convert Binary to Decimal
To reconvert binary to decimal the format is:
```
First Remainder Value * 2^n + ...... + Last Remainder Value * 2^0
```
where n keeps decreasing by 1 until it reaches 0 and the remainder values are the binary digits, found from left to right. 
In this case, it is:
```
1*2^2 + 1*2^1 + 0*2^0 = 6
```

### Implementing the Code
Every time, the decimal number is divided, the remainder numbers after each division must be saved. A list data type variable is initiated and the values are appended to the list.
```
if __name__ == '__main__':
    n = int(input().strip())
    remainder_list = []
```

Every time, the script is executed, n is the variable that is given as the decimal value. This variable needs to be divided until it the final result is 0. This can be done with a while-loop:
```
if __name__ == '__main__':
    n = int(input().strip())
    remainder_list = []

    
    while n != 0:
        remainder = n % 2
        remainder_list.append(remainder)
        
        n //= 2
```
In the for-loop, after every division iteration, the modulus operation is used to find the remainder and append the value to the list. <br>
<br>
After, the remainder list is finalized, it needs to be reversed, since the last remainder value is the first value that is used to be converted from binary to decimal. After reversing the order of the list, the values is added to a new variable or an empty string.
```
if __name__ == '__main__':
    n = int(input().strip())
    remainder_list = []

    
    while n != 0:
        remainder = n % 2
        remainder_list.append(remainder)
        
        n //= 2

    reverse_list = remainder_list[::-1]
    binary_string = ""

    for i in range(0, len(reverse_list)):
        binary_string += str(reverse_list[i])
```
Afterward, a for-loop was initiated to go through the binary string and keep track of the consecutive_one_count. If the consecutive_one_count is broken, then the other variable highest_score saves the oldest highest count until it is surpassed.

## Solution
```
#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    remainder_list = []
    
    while n != 0:
        remainder = n % 2
        remainder_list.append(remainder)
        
        n //= 2
    
    reverse_list = remainder_list[::-1]
    binary_string = ""
    for i in range(0, len(reverse_list)):
        # calculation = remainder_list[i] * (2**i)
        # total_sum += calculation 
        binary_string += str(reverse_list[i])
    
    consecutive_one_count = 0
    highest_score = 0
    
    for i in range(0, len(binary_string)):
        if binary_string[i] == '1':
            consecutive_one_count += 1
            
            if consecutive_one_count > highest_score:
                highest_score = consecutive_one_count 
        elif binary_string[i] == '0':
            consecutive_one_count = 0
            highest_score = highest_score
        else:
            pass
            
    
    print(highest_score)
```

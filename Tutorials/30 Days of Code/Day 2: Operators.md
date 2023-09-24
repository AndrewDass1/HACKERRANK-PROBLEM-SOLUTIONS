# Day 2: Operators
## Task
Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost. Round the result to the nearest integer. <br>
<br>
Link to the problem: https://www.hackerrank.com/challenges/30-operators/problem

## Explanation
This problem asks us to calculate the meal price as it gives us pre-defined variables to work with: meal_cost, tip_percent, and tax_percent. All calculations to find the meal_cost should be written in the function, and should return the total meal cost rounded to the nearest integer. Below is the function:
```
def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
```
In a function, the variables that are written in the parenthesis are already declared and as stated before, the variables meal_cost, tip_percent, and tax_percent are already declared. When the function is executed, it then asks for numerical numbers in place for each variable. There is no need to rewrite the variable in the function and ask it for an input. <br> <br>
To calculate the total meal cost, it requires summing the price of the meal, the tax percent for the meal and the tip percent of the meal. Both the tax and tip percentages are calculated by multiplying the specified decimal values from "tip_percent" and "tax_percent" to the meal cost. The function originally reads in integers as the tip_percent and tax_percent,  therefore, they must be divided by 100 to find the decimal values before multiplying it to the meal_cost to find the actual percentages. After finding the two percentages, sum it to the meal cost and use the round() function to round the cost to the nearest integer. 

```
def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    tip_percent_cost = meal_cost * (tip_percent/100)
    tax_percent_cost = meal_cost * (tax_percent/100)
    total_cost = meal_cost + tip_percent_cost + tax_percent_cost
    
    rounded_total_cost = round(total_cost)
    
    print(rounded_total_cost)
```

## Solution
```
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    tip_percent_cost = meal_cost * (tip_percent/100)
    tax_percent_cost = meal_cost * (tax_percent/100)
    total_cost = meal_cost + tip_percent_cost + tax_percent_cost
    
    rounded_total_cost = round(total_cost)
    
    print(rounded_total_cost)

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
```

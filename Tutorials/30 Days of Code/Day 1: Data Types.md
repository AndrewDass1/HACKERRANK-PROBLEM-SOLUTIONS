# Day 1: Data Types
## Task
Complete the code in the editor below. The variables i, d, and s are already declared and initialized for you. You must:

Declare 3 variables: one of type int, one of type double, and one of type String.
Read 3 lines of input from stdin (according to the sequence given in the Input Format section below) and initialize your 3 variables.
Use the + operator to perform the following operations:
1. Print the sum of i plus your int variable on a new line.
2. Print the sum of d plus your double variable to a scale of one decimal place on a new line.
3. Concatenate s with the string you read as input and print the result on a new line.

Link to the problem: https://www.hackerrank.com/challenges/30-data-types/problem

## Explanation
This problem is asking to declare three new variables: an integer, a float and a string. The new variables must be added to the previously declared variables that shares the same data type. Adding variables different data types causes an error which is why it is important to add the same variables with the same data type together. To make a new variable, the input() function is used to read a string data type statement. To read an integer or a decimal, the input() keyword can be casted with int() or float() to accept integer or decimal values respectively.
### Existing Variables
```
i = 4
d = 4.0
s = 'HackerRank '
```
### Declaring new Variables with input(), int() and float()
```
i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.
i2 = int(input(""))
d2 = float(input(""))
s2 = input("")
```
After declaring the new variables, add the new variables to the old variables. Make sure every variable that are being added to one another has the same data type.

### Adding the Variables Together
```
i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.
i2 = int(input(""))
d2 = float(input(""))
s2 = input("")

# Read and save an integer, double, and String to your variables.
i_statements = i + i2
d_statements = d + d2
s_statements = s + s2
```
Then, print the statements or results after adding the variables together.

### Solution
```
i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.
i2 = int(input(""))
d2 = float(input(""))
s2 = input("")

# Read and save an integer, double, and String to your variables.
i_statements = i + i2
d_statements = d + d2
s_statements = s + s2

# Print the sum of both integer variables on a new line.
print(i_statements)
# Print the sum of the double variables on a new line.
print(d_statements)
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s_statements)
```

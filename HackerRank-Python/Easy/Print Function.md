# Task
The included code stub will read an integer, n, from STDIN. <br>
<br>
Without using any string methods, try to print the following: <br>
123...n<br>
<br>
Note that "" represents the consecutive values in between.<br>
<br>
**Example** <br>
Print the string 12345 <br>
<br>

**Input Format** <br>
The first line contains an integer n <br>
<br>

**Constraints** <br>
1 <= n <= 150 <br>

**Output Format** <br>
Print the list of integers from through as a string, without spaces.

# Procedure
1. Declare variable n to take the input to be any number:
```
n = int(input(""))
```
2. Initiate a for loop to go through starting with the number 1 to specified integer n:
```
for i in range(1, n+1):
  print(i, end="")
```

# Solution
```
n = int(input())
    
for i in range(1, n+1):
  print(i, end="")
```

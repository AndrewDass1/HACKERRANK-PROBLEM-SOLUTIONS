## Task
The provided code stub reads and integer, n, from STDIN. For all non-negative integers i<n, print i^2 <br>
<br>
**Example**<br>
n=3 <br>
<br>
The list of non-negative integers that are less than n=3 is [0,1,2]. Print the square of each number on a separate line. <br>
```
0
1
4
```

**Input Format**<br>
The first and only line contains the Integer, n. <br>
<br>
**Constraints** <br>
1 <= n <= 20 <br>
<br>
**Output Format** <br>
Print n lines, one corresponding to each i

## Procedure
1. Declare n as the variable to take any integer as an input
```
n = int(input(""))
```
2. Initiate a for loop to go through numbers 0 to n and print out the square of each iteration
```
for i in range(0, n):
  print(i**2)
```

## Solution
if __name__ == '__main__':
    n = int(input())
    
    for i in range(0, n):
        print(i**2)

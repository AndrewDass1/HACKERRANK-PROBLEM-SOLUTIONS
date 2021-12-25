# Cut 1

## Task 
Given N lines of input, print the 3rd character from each line as a new line of output. It is guaranteed that each of the n lines of input will have a 3rd character.

## Procedure
1. Concatenate a file:
```
cat >> file.txt
```
2. Use the cut command on the file to print out the 3rd character of each line in the specified document or file:
```
cut file.txt -c 3
```

## Solution
```
cat >> file.txt
cut file.txt -c 3
```

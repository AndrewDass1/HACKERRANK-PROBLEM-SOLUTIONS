# A Personalized Echo

## Task 
Write a bash script which accepts name as input and displays the greeting "Welcome (name)"

## Procedure
1. In Bash, a variable can be declared with the command "read" as shown below:
```
read name
```
After using the command read, a name variable can be assigned as a string 
2. To print a statement use the echo command to print out the string and name:
```
echo "Welcome" "$name"
```
When a variable is declared in bash, a $ sign must be declared before the variable to print out its assigned value

## Solution
```
read name
echo "Welcome" "$name"
```

# Task
Problem Link: https://www.hackerrank.com/challenges/python-mutations/problem
# Procedure
1. Initalize a variable that will contain the new string with the replaced character
```
new_string = ""
```

2. Create a for loop to go through the original string:
```
index = 0
for i in string:
    ....
    index+=1
```

3. In the for loop, incorporate an if and else statement to go through the original string. The index variable is designed to increase by 1, but when it equals the same value as position, then the character will be added to the new_string variable as opposed to the what letter is found in the string variable.  
```
index = 0
for i in string:
    if index == position:
         new_string = new_string + character
    else:
         new_string = new_string + string[index]
    index+=1
```

4. Return the function
```
return new_string
```

# Solution
```
def mutate_string(string, position, character):
    new_string = ""
    index = 0
    
    for i in string:
        if index == position:
            new_string = new_string + character
        else:
            new_string = new_string + string[index]
        index+=1
        
    return new_string
```

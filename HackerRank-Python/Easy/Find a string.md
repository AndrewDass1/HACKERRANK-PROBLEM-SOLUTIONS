# Task
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left. <br>
<br>
NOTE: String letters are case-sensitive. <br>
<br>
Input Format <br>
<br>
The first line of input contains the original string. The next line contains the substring. <br>

Constraints <br>
<br>
<br>
Each character in the string is an ascii character. <br>
<br>
Output Format <br>
<br>
Output the integer number indicating the total number of occurrences of the substring in the original string. <br>
<br>
# Procedure 
In this challenge, it is asked to create a function called count_substring to take two variables string and substring to see how many times the word substring 
appears in string. <br>
<br>
1. First define the function: <br>
```
def count_substring(string, sub_string):
```

2. If the variable substring is supposed to be found withing string, then its length must be less than the variable string length. A 
while loop can be implemented to prevent this.
```
  while(len(sub_string)>=len(string)):
    sub_string = input('')
```

3. Next variables were declared called: <br>
   substring_length: to receive the length of the sub_string <br>
   start: Begins at index 0 <br>
   second_start: To read substring_length index <br>
   find_match : A substring counter checker to see if there was a match found within the string
```
substring_length = len(sub_string)
  start = 0
  second_start = len(sub_string)
  
  find_match = 0
```

4. Implement a for loop to iterate through string's indexes to see if it is equal to the substring provided. If there is a match, the find_match counter will be updated 
5. and find_match is the variable that will be returned from the function. 
```
for i in range(0, len(string)):
    if string[start:second_start] == sub_string:
      find_match += 1

    start += 1

    if(second_start == len(string) ):
      second_start = len(string)
    else:
      second_start += 1
     
  return find_match
```

# Solution
```
def count_substring(string, sub_string):


  while(len(sub_string)>=len(string)):
    sub_string = input('')

  substring_length = len(sub_string)
  start = 0
  second_start = len(sub_string)

  find_match = 0


  for i in range(0, len(string)):
    if string[start:second_start] == sub_string:
      find_match += 1

    start += 1

    if(second_start == len(string) ):
      second_start = len(string)
    else:
      second_start += 1
     
  return find_match
```

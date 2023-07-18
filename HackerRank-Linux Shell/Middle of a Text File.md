# Middle of a Text File

## Task 
Display the lines (from line number 12 to 22, both inclusive) of a given text file. <br>
<br>
Link to the Problem: https://www.hackerrank.com/challenges/text-processing-in-linux---the-middle-of-a-text-file/problem 
## Explanation
To print the first few lines of a file, the head command is used. To print the last lines of a file, the tail command is used. The head and tail commands can be used in conjunction with a pipe or "|" to print a range of lines. <br>
<br>

First start by writing "head -22". head -22 prints the first 22 lines of the file. 
```
head -22
```
Now after the -22, include a "|" to continue the statement. After the "|", the tail command will now be used and the specific statement "tail +12" will be written. tail +12 means lines 12 and everything after would be printed out. Due to specifying "head -22" earlier, only the lines starting from 12 to 22 will now be printed out.  

## Final Solution
```
head -22 | tail +12
```

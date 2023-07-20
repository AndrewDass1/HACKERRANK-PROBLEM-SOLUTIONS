# Paste-1
## Task
In this challenge, we practice using the paste command to merge lines of a given file. You are given a CSV file where each row contains the name of a city and its state separated by a comma. Your task is to replace the newlines in the file with semicolons as demonstrated in the sample. <br>
<br>
Link to the Problem: https://www.hackerrank.com/challenges/paste-1/problem
## Explanation
To allow existing text or content to appear on the same line, "paste -s" is used. "-s" means serial which is to merge many small lines to longer lines. To separate the content by any text, the file can be delimited with "-d". After delimiting the file, it takes any text or characters written after this parameter to separate the lines.
## Final Solution
```
paste -s -d ';'
```

# 'Tr' Command #2
## Task
In this challenge, we practice using the tr command because it is a useful translation tool in Linux. In a given fragment of text, delete all the lowercase characters a-z. <br>
<br>
Link to the Problem: https://www.hackerrank.com/challenges/text-processing-tr-2/problem
## Explanation
The 'tr' command can also delete any unwanted characters with '-d'. Any characters including lowercase letters or a range of letters can be specified to be deleted by using the option '-d' to dispose of them. 

## Final Solution
```
tr -d "a-z"
```

# Tr Command #1
## Task
In this challenge, we practice using the tr command because it is a useful translation tool in Linux. In a given fragment of text, replace all parentheses () with box brackets []. <br>
<br>
Link to the Problem: https://www.hackerrank.com/challenges/text-processing-tr-1/problem
## Explanation
The 'tr' command stands for translate. This command translates strings or characters to become other strings or characters. Shown below is how the 'tr' command is utilized:
```
tr 'text' 'new_text'
```
Executing the tr command changes the 'text' which is a string data type and it will be replaced by what is contained in 'new_text'. Below is how to replace all parentheses for brackets:
## Final Solution
```
tr '()' '[]'
```

# 'Uniq' Command #2

## Task
Given a text file, count the number of times each line repeats itself. Only consider consecutive repetitions. Display the space separated count and line, respectively. There shouldn't be any leading or trailing spaces. Please note that the uniq -c command by itself will generate the output in a different format than the one expected here. <br>
<br>
Link to the problem: https://www.hackerrank.com/challenges/text-processing-in-linux-the-uniq-command-2/problem

## Explanation
The command 'uniq' searches and removes all repeated lines that appear after the first line that has that same text. The command 'uniq -c' shows all duplicate lines and 'cut -c7-' cuts the characters to show the expected output.

## Final Solution
```
uniq -c | cut -c7-
```

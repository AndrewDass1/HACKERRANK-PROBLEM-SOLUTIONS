# Sort Command #4
## Task
You are given a file of text, where each line contains a number (which may be either an integer or have decimal places). There will be no extra characters other than the number or the newline at the end of each line. Sort the lines in descending order - - such that the first line holds the (numerically) largest number and the last line holds the (numerically) smallest number.

Link to the Problem: https://www.hackerrank.com/challenges/text-processing-sort-4/problem
## Explanation
In Bash, using the command 'sort' arranges all the string data type content in increasing order by default. There are additional parameters to sort the content such as numbers in increasing or decreasing order. To sort numbers in increasing order, the '-n' parameter is used. To sort the numbers in decreasing order, both the '-n' and '-r' parameters are used together. 
## Final Solution
```
sort -n -r
```

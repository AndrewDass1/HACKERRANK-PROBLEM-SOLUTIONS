# 'Uniq' Command #1
## Task
In this challenge, we practice using the uniq command to eliminate consecutive repetitions of a line when a text file is piped through it. Given a text file, remove the consecutive repetitions of any line. <br>
<br>
Link to the Problem: https://www.hackerrank.com/challenges/text-processing-in-linux-the-uniq-command-1/problem

## Explanation
The command 'uniq' searches and removes all repeated lines that appea after the first line that has that same text. In this problem, the sample input is:
```
00
00
01
01
00
00
02
02
```
Using 'uniq' will remove the second line, the fourth line, the sixth line and the eighth line. The final result would appear like this:
```
00
01
00
02
```
There is another '00' since after '01' since in the original input, there are two '01' that separated the '00' text from one another. 'uniq' disposes of all of the same content that already appeared in the line before it.
## Final Solution
```
uniq
```
To use the uniq command in the Terminal, the file name must be specified as well in a format shown below:
```
uniq file_name.extension
```

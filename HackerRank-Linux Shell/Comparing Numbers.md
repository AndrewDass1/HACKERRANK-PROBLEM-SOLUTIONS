# Comparing Numbers

## Task
Given two integers, X and Y, identify whether X < Y or X > Y or X = Y. <br>
<br>
Exactly one of the following lines: <br>
- X is less than Y
- X is greater than Y
- X is equal to Y

## Procedure
1. Declare X and Y as integer data types:
```
read X
read Y
```
2. Declare an if elif else statements to compare X and Y integer values and output the correct statement regarding whether X is less, greater or equal to Y:
```
if (($X > $Y)); 
then
echo X is greater than Y; 

elif (($X == $Y)); 
then
echo X is equal to Y;
 
elif (($X < $Y)); 
then
echo X is less than Y; 
fi
```

## Solution
```
read X
read Y
if (($X > $Y)); 
then
echo X is greater than Y; 

elif (($X == $Y)); 
then
echo X is equal to Y;
 
elif (($X < $Y)); 
then
echo X is less than Y; 
fi
```

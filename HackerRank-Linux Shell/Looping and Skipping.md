# Looping and Skipping

## Task
Your task is to use for loops to display only odd natural numbers from 1 to 99. 

## Procedure
1. To make a for loop in bash, the syntax is shown below:
```
for _ in {start..end..increment}
do
  echo ...
done
```

* _: Declared variable
* start: Number it begins from 
* end: Number it stops at
* increment: The for loop follows this to either increase or decrease during every iteration
* ... : Statement to print out in the for loop

To print every odd number from the range 1 to 99, the following for-loop can be used:
```
for i in {1..99..2}
do
  echo $i
done
```

# Solution
```
for i in (1..99..2}
do
  echo $i
done
```

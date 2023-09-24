# Day 4: Class vs Instance
## Task
Write a Person class with an instance variable, age, and a constructor that takes an integer, initialAge, as a parameter. The constructor must assign initialAge to age after confirming the argument passed as initialAge is not negative; if a negative argument is passed as initialAge, the constructor should set age to 0 and print Age is not valid, setting age to 0. In addition, you must write the following instance methods:

1. yearPasses() should increase the age instance variable by 1.
2. amIOld() should perform the following conditional actions:
* If age < 13, print 'You are young.'.
* If age >=13 and age < 18, print 'You are a teenager.'.
* Otherwise, print 'You are old.'.

Link to the problem: https://www.hackerrank.com/challenges/30-class-vs-instance/problem 

## Explanation
It is specified that code only needs to be added or modified in the 'Person' class:

```
class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
        # Increment the age of the person in here
```

A variable called 'initialAge' must be declared. 
```
class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        self.initialAge = initialAge
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
        # Increment the age of the person in here
```
initialAge is set equal to 'self.initialAge' since self is a parameter in Python when an instance variable outside the class is declared to use the class, it substitutes the name of the instance variable in place of self to use the class's attributes or code in the functions. Any variables created in the class with self, can also be used in other functions that uses self too.

For the rest of the code, many if and else statements were used to set and check for the conditions specified in the 'Task' and a counter to increase age by one was implemented.

## Solution
```
class Person:
    def __init__(self,initialAge):
        self.initialAge = initialAge
        if self.initialAge > 0:
            self.age = self.initialAge
        else:
            print("Age is not valid, setting age to 0.")
            self.age = 0
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age < 13:
            print("You are young.")
        elif self.age >= 13 and self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.") 
    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1
```

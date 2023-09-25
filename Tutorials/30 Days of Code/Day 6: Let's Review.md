# Day 6: Let's Review
## Task
Given a string, S, of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail). <br> <br>

Link to the problem: https://www.hackerrank.com/challenges/30-review-loop/problem

## Explanation
Run the Python script is executed, a variable must be declared for it to ask the user for how many words they want to input. In this script, the variable "how_many_words" asks the user to input as much words as specified. This is also done by integrating a for-loop with it.
```
how_many_words = int(input(""))

for i in range(0, how_many_words):
    enter_word = input("")
```

Every word that is inputted, the length of that word must be taken account of, to integrate another for-loop to further analyze each index of the word and separate the even and the odd indexes.
```
how_many_words = int(input(""))

for i in range(0, how_many_words):
    enter_word = input("")
    
    len_of_word = len(enter_word)
```
A possible way is to separate the even and odd indexes is to make two new empty string variables to hold this data. The for-loop goes through the entire inputted word and every even or odd index can be added to the appropriate variable. An if-and-else statement with a modulus condition is set to identify whether each index of the word is either even or odd.

## Solution
```
how_many_words = int(input(""))

for i in range(0, how_many_words):
    enter_word = input("")
    
    len_of_word = len(enter_word)
    
    even_indexes = ""
    odd_indexes = ""
    
    for i in range(0, len_of_word):
        if i % 2 == 0:
            even_indexes += enter_word[i]
        else:
            odd_indexes += enter_word[i]
        
    print(even_indexes, odd_indexes)
```

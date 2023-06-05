#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    length_of_arr = len(arr)
    positive_count = 0
    negative_count = 0
    zero_count = 0
    index = 0
    
    for i in range(0, len(arr)):
        if arr[index] > 0:
            positive_count += 1
        elif arr[index] == 0:
            zero_count += 1
        elif arr[index] < 0:
            negative_count += 1
        else:
            pass
        index += 1
        
    positive_percentage = positive_count / length_of_arr
    negative_percentage = negative_count / length_of_arr
    zero_percentage = zero_count / length_of_arr

    print(positive_percentage)
    print(negative_percentage)
    print(zero_percentage)

    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

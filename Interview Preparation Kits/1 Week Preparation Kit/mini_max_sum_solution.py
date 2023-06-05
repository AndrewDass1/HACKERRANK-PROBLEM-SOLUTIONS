#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    sums = []
    current_sum = 0
    
    index = 0
    position = 0
    
    while position < len(arr):
        if index == position:
            pass
        else:
            current_sum = current_sum + arr[index]
            # print(current_sum)
        index += 1
        
        if index == len(arr):
            sums.append(current_sum)
            current_sum = 0
            index = 0
            position += 1
            
    #print(sums)
    sorted_sums = sorted(sums)
    
    print(sorted_sums[0], sorted_sums[len(sorted_sums)-1])   
        
        
            
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n): 

    #my code starts here      
    number_of_periods = n
    print("number_of_periods arxh =",number_of_periods)
    height = 1 
    
    for i in range(0,number_of_periods):       
        if ((i%2) == 0):            
            height = height*2 
        elif ((i%2) == 1):
            height += 1
            
       
    return height

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()

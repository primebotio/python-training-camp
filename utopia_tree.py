#!/bin/python3
# -*- coding: utf-8 -*-

import os

def utopianTree(number_of_periods): 
    #my code starts here     
    height = 1 
    
    for i in range(number_of_periods):       
        if i%2 == 0:            
            height = height*2 
        else:
            height += 1
       
    return height

if __name__ == '__main__':

    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:       
        test_cases = int(input())
        for _ in range(test_cases):
            n = int(input())

            result = utopianTree(n)

            fptr.write(str(result) + '\n')

        

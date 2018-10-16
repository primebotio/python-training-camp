#!/usr/bin/env python3.5
from __future__ import print_function
from functools import reduce
import math
import os
import random
import re
import sys
import logging
#import ipdb

logging.basicConfig(level=logging.WARN, format='%(levelname)s- %(message)s')



def read_file(filename):
    file_obj = open(filename, "r")
    n = file_obj.readline()

    if int(n) not in range(1,11):
        sys.stderr.write("Number of testcases is out of range. Exiting... exit(1)\n")
        exit(1)



    array = []
    for i in range(int(n)):
        t = file_obj.readline()
        if int(t) not in range(60):
            sys.stderr.write("Number of cycles is:\n")
            sys.stderr.write(t)
            sys.stderr.write("Number of cycles out of range. Exiting... exit(2)\n")
            exit(2)
        array.append(int(t))

    return array

def utopianTree(n):
    if(n==0):
        return 1

    H = 1
    for i in range(1,n+1):
        if i%2==1:
            H *= 2
        elif i%2==0:
            H += 1

    return H


if __name__ == '__main__':

    # INFO
    # I read the testcase files with function read file
    # which outputs an anrray
    # FUNCTIONALITY
    # Change the number before the . to pick test case [0-2]
    t = read_file('testcases/testcase0.txt')

    logging.debug(len(t))
    for i in range(len(t)):
        logging.debug(t[i])


        result = utopianTree(t[i])

        print(result)


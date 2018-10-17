#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import math
import os
import re
import sys
import logging
#import ipdb

def plusMinus(m):
   # sz = len(m)
    n=0
    z=0
    p=0
    for i in range(len(m)):
        if m[i] < 0 :
            n += 1
        elif m[i] == 0:
            z += 1
        else:
            p += 1

    return  n/len(m) , z/len(m) , p/len(m)



logging.basicConfig(level=logging.WARN, format='%(levelname)s- %(message)s')
if __name__ == '__main__':
    with open("testcases/testcase0.txt") as file_obj:
        data = file_obj.readlines()
    n = int(data[0])
    arr = list(map(int, data[1].rstrip().split()))
    
    n,z,p = plusMinus(arr)
    
    print ("%6f" %p)
    print ("%6f" %n)
    print ("%6f" %z)



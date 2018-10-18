#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
from functools import reduce
import math
import os
import re
import sys
import logging
#import ipdb


def plusMinusReduced(l):
    n = len([ num for num in l if num < 0])
    z = len([ num for num in l if num == 0])
    p = len([ num for num in l if num > 0])
    return  n/len(l), z/len(l) , p/len(l)

logging.basicConfig(level=logging.WARN, format='%(levelname)s- %(message)s')
if __name__ == '__main__':
    with open("testcases/testcase0.txt") as file_obj:
        data = file_obj.readlines()
    n = int(data[0])
    arr = list(map(int, data[1].rstrip().split()))
    
    n,z,p = plusMinusReduced(arr)
    
    print ("%6f" %p)
    print ("%6f" %n)
    print ("%6f" %z)



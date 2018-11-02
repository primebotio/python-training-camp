#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import math
import os
import random
import re
import sys



def gameOfThrones(s):
    s = s.rstrip('\n')
    counter = 0
    lettermap = dict(zip("abcdefghijklmnopqrstuvwyz",range(0,26)))
    times_found = [0]*26

    for c in s:
        if c in lettermap:
            times_found[lettermap[c]] += 1

    #print(times_found)
    for num in times_found:
        if num % 2 != 0:
            counter += 1
        if counter == 2:
            return False

    return True



if __name__ == '__main__':
    with open("testcases/testcase3.txt") as file_obj:
        data = file_obj.readlines()
    s = data[0]
    # print (s)

    result = gameOfThrones(s)

    if result:
        print('Yes')
    else:
        print('No')












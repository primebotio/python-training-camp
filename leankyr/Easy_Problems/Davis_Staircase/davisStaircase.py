#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import sys
count = 0
substairs = []
from itertools import combinations
# say I can only go up 1 stair at a time
def stepPerms(n):

    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return stepPerms(n - 1) + stepPerms(n - 2) + stepPerms(n -3)



if __name__ == '__main__':
    with open("testcases/testcase1.txt") as file_obj:
        data = file_obj.readlines()
    s = int(data[0])
    # print (s)


    for i in range(s):
        n = int(data[i+1])
        #print (n)
        res = stepPerms(n)
        print (res%10000000007)



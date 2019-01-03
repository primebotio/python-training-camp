#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import sys
d = {1:1,2:2,3:4}
def stepPerms(n):
    global d
    if n in d:
        return d[n]
    else:
        result = stepPerms(n - 3) + stepPerms(n - 2) + stepPerms(n - 1)
        d[n] = result
        return d[n]


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



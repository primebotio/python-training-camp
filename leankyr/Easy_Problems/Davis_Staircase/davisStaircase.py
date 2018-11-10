#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import sys
ways_list = list()
way = list()
step = 1
# say I can only go up 1 stair at a time
def stepPerms(n):
    global way
    global step
    if n == 0:
        ways_list.append(way)
        return way
    else:
        way.append(step)
        return stepPerms(n-step)

if __name__ == '__main__':
    with open("testcases/testcase1.txt") as file_obj:
        data = file_obj.readlines()
    s = int(data[0])
    # print (s)


    for i in range(s):
        n = int(data[i+1])
        #print (n)
        res = stepPerms(n)
        print (res)
        way.clear()











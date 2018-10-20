#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import math
import re
import sys

# Complete the birthday function below.
    
def birthday(s, d, m):
    c = 0
    for i in range(len(s)):
        l = list()
        for j in range(i,len(s)):
            l.append(s[j])
            if len(l) == m and sum(l) == d:
                c += 1
                break
            elif len(l) > m:
                break
    return c


if __name__ == '__main__':
    file_num = sys.argv[1]
    with open("testcases/testcase"+file_num+".txt") as file_obj:
        data = file_obj.readlines()
    #data are ready for use
    n = int(data[0].rstrip())
    if n not in range(1,100):
        sys.stderr.write(" too big chocolate")
        exit(1)
    s = list(map(int, data[1].rstrip().split()))
    if max(s) > 5 or min(s) < 1:
        sys.stderr.write("too big in on square")
        exit(1)
    dm = data[2].rstrip().split()
    d = int(dm[0])
    if d < 1 or d > 31:
        sys.stderr.write("not a day of month")
        exit(1)

    m = int(dm[1])
    if m < 1 or m > 12:
        sys.stderr.write("not a terran month")
        exit(1)

    result = birthday(s, d, m)
    print(result)




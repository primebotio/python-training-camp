#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import math
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    return

if __name__ == '__main__':
    file_num = sys.argv[1]
    with open("testcases/testcase"+file_num+".txt") as file_obj:
        data = file_obj.readlines()
    #data are ready for use
    n = int(data[0].rstrip())
    s = list(map(int, data[1].rstrip().split()))
    dm = data[2].rstrip().split()
    d = int(dm[0])
    m = int(dm[1])

    result = birthday(s, d, m)




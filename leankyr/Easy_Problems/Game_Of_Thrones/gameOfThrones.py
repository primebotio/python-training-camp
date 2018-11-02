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
    st = set()
    for c in s:
        if c in st:
            continue
        #print (s.count(c))
        if s.count(c) % 2 != 0 and c not in st:
            st.add(c)
            counter += 1
            if counter == 2:
                return False

    print (counter)
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












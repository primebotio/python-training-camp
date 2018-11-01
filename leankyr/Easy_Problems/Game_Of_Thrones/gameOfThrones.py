#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import math
import os
import random
import re
import sys



NO_OF_CHARS = 256

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


def canFormPalindrome(st) :

    # Create a count array and initialize   
    # all values as 0 
    count = [0] * (NO_OF_CHARS)

    # For each character in input strings, 
    # increment count in the corresponding 
    # count array 
    for i in range( 0, len(st)) :
        count[ord(st[i])] = count[ord(st[i])] + 1

    # Count odd occurring characters 
    odd = 0

    for i in range(0, NO_OF_CHARS ) :
        if (count[i] & 1) :
            odd = odd + 1

        if (odd > 1):
            return False

    # Return true if odd count is 0 or 1,  
    return True




if __name__ == '__main__':
    with open("testcases/testcase3.txt") as file_obj:
        data = file_obj.readlines()
    s = data[0]
    # print (s)

    result = canFormPalindrome(s)

    if result:
        print('Yes')
    else:
        print('No')












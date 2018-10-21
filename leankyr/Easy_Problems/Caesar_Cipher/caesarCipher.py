#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import sys

def caesarCipher(s, k):
    crypts = ''
    k = k%26
    for c in s:
        ### HOTFIX ####
        if c.isupper() and ord(c) == 90 - k:
            crypts += 'Z'
            continue
        if c.islower() and ord(c) == 122 - k:
            crypts += 'z'
            continue
        ### END HOTFIX ###
        
        
        
        if ord(c) in range(ord('A'),ord('Z')+1):
            c = chr((ord(c) + k)%ord('Z'))
            if ord(c) < ord('A'):
                c = chr(ord(c) + ord('A')-1)
            crypts += c
        elif ord(c) in range(ord('a'),ord('z')+1):
            c = chr((ord(c) + k)%ord('z'))
            if ord(c) < ord('a'):
                c = chr(ord(c) + ord('a')-1)
            crypts += c
        else:
            crypts += c
            continue
    return crypts




if __name__ == '__main__':
    with open("testcases/testcase2.txt") as file_obj:
        data = file_obj.readlines()

    n = int(data[0])
    s = data[1]
    k = int(data[2])

    print(caesarCipher(s, k))


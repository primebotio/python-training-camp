#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import sys
from collections import deque

def caesar_cipher(s, k):
    capitals_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_alphabet = capitals_alphabet.lower()

    #alphabet = capitals_alphabet + lowercase_alphabet

    # deque takes as argument the think I want to turn into deque
    encrypted_caps = deque(capitals_alphabet)
    encrypted_caps.rotate(-k)

    encrypted_lower = deque(lowercase_alphabet)
    encrypted_lower.rotate(-k)

    # When I "add" two lists like strings it appends the second to the right of the first
    keys = list(capitals_alphabet) + list(lowercase_alphabet)
    # print (keys)
    vals = list(encrypted_caps) + list(encrypted_lower)
    # print (vals)
    lettermap = dict(zip(keys,vals))

    encrypted_string = ''

    for c in s:
        if c in lettermap: # or in lettermap.keys()
            encrypted_string += lettermap[c]
        else:
            encrypted_string += c

    return encrypted_string



if __name__ == '__main__':
    with open("testcases/testcase0.txt") as file_obj:
        data = file_obj.readlines()

    n = int(data[0])
    s = data[1]
    k = int(data[2])

    print(caesar_cipher(s, k))


#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import sys

def caesarCipher(s, k):
    k = k%26
    # Caps2integers Mappin
    Caps2integers = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(0,26)))
    integers2Caps = dict(zip(range(0,26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    
    letters2integers = dict(zip("abcdefghijklmnopqrstuvwxyz",range(0,26)))
    integers2letters = dict(zip(range(0,26),"abcdefghijklmnopqrstuvwxyz"))
    
    # print (L2I['z'])
    # print (I2L[52])

    encrypted_str = ''
    for char in s:
        if char in Caps2integers:
            char = integers2Caps[(Caps2integers[char] + k)%26]
        elif char in letters2integers:
            char = integers2letters[(letters2integers[char] + k)%26]
        else:
            pass
        encrypted_str += char

    return encrypted_str



if __name__ == '__main__':
    with open("testcases/testcase2.txt") as file_obj:
        data = file_obj.readlines()

    n = int(data[0])
    s = data[1]
    k = int(data[2])

    print(caesarCipher(s, k))


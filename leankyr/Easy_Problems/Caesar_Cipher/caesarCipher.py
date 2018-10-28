#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import sys

def caesarCipher(s, k):
    k = k%26
    # L2I Mappin
    L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(0,26)))
    I2L = dict(zip(range(0,26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    
    l2i = dict(zip("abcdefghijklmnopqrstuvwxyz",range(0,26)))
    i2l = dict(zip(range(0,26),"abcdefghijklmnopqrstuvwxyz"))
    
    # print (L2I['z'])
    # print (I2L[52])

    encrypted_str = ''
    for c in s:
        if c in L2I:
            c = I2L[(L2I[c] + k)%26]
        elif c in l2i:
            c = i2l[(l2i[c] + k)%26]
        else:
            pass
        encrypted_str += c

    return encrypted_str



if __name__ == '__main__':
    with open("testcases/testcase0.txt") as file_obj:
        data = file_obj.readlines()

    n = int(data[0])
    s = data[1]
    k = int(data[2])

    print(caesarCipher(s, k))


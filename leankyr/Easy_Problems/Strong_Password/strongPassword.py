#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import sys
import re

#from collections import Counter


def minimum_number(n, password):
    # sets of available characters
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"


    stuff_to_add = 4

    for c in password:
        if c in lower_case:
            stuff_to_add -= 1
            break

    for c in password:
        if c in upper_case:
            stuff_to_add -= 1
            break

    for c in password:
        if c in numbers:
            stuff_to_add -= 1
            break

    for c in password:
        if c in special_characters:
            stuff_to_add -= 1
            break

    print (stuff_to_add)

    if n + stuff_to_add >= 6:
        return stuff_to_add
    else:
        return 6 - n






if __name__ == '__main__':
    with open("testcases/testcase0.txt") as file_obj:
        data = file_obj.readlines()

    n = int(data[0])
    password = data[1]

    answer = minimum_number(n, password)

    print(answer)



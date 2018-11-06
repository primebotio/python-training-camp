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

    return





if __name__ == '__main__':
    with open("testcases/testcase1.txt") as file_obj:
        data = file_obj.readlines()

    n = int(data[0])
    password = data[1]

    answer = minimum_number(n, password)

    print(answer)



#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import sys

from collections import Counter

def game_of_thrones(s):
    s = s.rstrip('\n')

    count_letters = Counter(s)

    counter = 0

    values = list(count_letters.values())

    for num in values:
        if num % 2 != 0:
            counter += 1
        if counter == 2:
            return False

    return True



if __name__ == '__main__':
    with open("testcases/testcase2.txt") as file_obj:
        data = file_obj.readlines()
    s = data[0]
    # print (s)

    result = game_of_thrones(s)

    if result:
        print('Yes')
    else:
        print('No')












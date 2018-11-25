#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-



def icecreamParlor(m, arr):
    pass


if __name__ == '__main__':
    with open("testcases/testcase0.txt") as file_obj:
        data = file_obj.readlines()

    t = int(data[0])

    for t_itr in range(t):
        m = int(data[t_itr + 1] )

        n = int(data[t_itr + 2])

        arr = list(map(int, data[t_itr + 3].rstrip().split()))
        
        print (arr)
        result = icecreamParlor(m, arr)

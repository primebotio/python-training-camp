#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import operator

def icecreamParlor(m, arr):

    d = dict()
    for i in range(len(arr)):
        d[i] = arr[i]

    sorted_d = sorted(d.items(), key=operator.itemgetter(1))

    #sorted_d = dict(zip(sorted_d[:][0],sorted_d[:][1]))
    #sorted_d = {k:v for k,v in sorted_d}
    #print (sorted_d)

    #print (sorted_d[1])
    #arr.sort()

    #t1 = sorted_d[1]

    found = False
    for t1 in sorted_d:
        for t2 in sorted_d:
            if t1[1] + t2[1] > m:
                break
            if t1[1] + t2[1] == m and t1[0] != t2[0]:
                k1 = t1[0]
                k2 = t2[0]
                found = True
                break
        if found:
            break

    ret_val = list()
    ret_val.append(k1 + 1)
    ret_val.append(k2 + 1)
    ret_val.sort()
    return ret_val











if __name__ == '__main__':
    with open("testcases/testcase0.txt") as file_obj:
        data = file_obj.readlines()

    t = int(data[0])
    for t_itr in range(0,3*t,3):

        m = int(data[t_itr + 1])

        n = int(data[t_itr + 2])

        arr = list(map(int, data[t_itr + 3].rstrip().split()))

        result = icecreamParlor(m, arr)

        print (result)

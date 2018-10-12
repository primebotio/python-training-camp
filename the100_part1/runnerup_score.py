#!/bin/python3
# -*- coding: utf-8 -*-

def findrunnerupscore(n,arr):

    maximum = max(arr)
    for i in range(len(arr)):
        if arr[i] == maximum :
            arr[i] = -1000
    
    rnrup = max(arr)

    return rnrup


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    result = findrunnerupscore(n, arr)
    print(result)

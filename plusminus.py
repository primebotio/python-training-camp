#!/bin/python3
# -*- coding: utf-8 -*-

import os

def plusMinus(arr):
    negatives=0
    positives=0
    zeros=0
    #size = len(arr)
    
    for i in range(len(arr)):
        if arr[i]>0:
            positives+=1
        elif arr[i]<0:
            negatives+=1
        else:
            zeros+=1
    
    print(positives/len(arr))
    print(negatives/len(arr))
    print(zeros/len(arr))

    return 0

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)

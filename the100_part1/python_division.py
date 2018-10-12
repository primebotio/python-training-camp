#!/bin/python3
# -*- coding: utf-8 -*-

def integerdivision(a,b):
    c = a//b
    return c

def floatdivision(a,b):
    c = a/b
    return c


if __name__ == '__main__':
    a = int(input())
    b = int(input())

    result1 = integerdivision(a,b)
    result2 = floatdivision(a,b)
    
    print(result1)
    print(result2)

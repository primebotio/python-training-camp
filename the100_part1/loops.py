#!/bin/python3
# -*- coding: utf-8 -*-

#1 <= N <= 20
def loop(N):
    for i in range(N):
        print(i**2)

if __name__ == '__main__':
    n = int(input())
    loop(n)
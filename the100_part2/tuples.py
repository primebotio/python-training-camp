#!/bin/python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    n = int(input())
    mylist = []
    integers = input().split()

    mylist = list(map(int, integers))
    finaltup = tuple(mylist)
   
    print(hash(finaltup))



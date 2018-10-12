#!/bin/python3
# -*- coding: utf-8 -*-

#n integer and 1<= N <= 100
N = int(input())

if N%2==1:    
    print("Weird")
elif N%2==0 and N>=2 and N<=5 :    
    print("Not Weird")
elif N%2==0 and N>=6 and N<=20:   
    print("Weird")
else:    
    print("Not Weird")


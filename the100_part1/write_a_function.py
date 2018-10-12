#!/bin/python3
# -*- coding: utf-8 -*-

def is_leap(year):
    leap = False
    while True:
        if year%4 == 0 :            
            if year%100 == 0 :                 
                if year%400 == 0 :                    
                    leap = True 
                    return leap
                else :
                    return leap
            else :                
                leap = True
                return leap
        else :
            return leap


    return leap

year = int(input())
print(is_leap(year))

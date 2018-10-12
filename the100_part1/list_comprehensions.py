#!/bin/python3
# -*- coding: utf-8 -*-

#se ayth thn askhsh 8elw exhghsh ths ekfwnhshs kai tou etoimou kwdika 
#thn ekana diais8htika kai me trial and error 
def comprehension(X, Y, Z, N):

    mylist = []
    for i in range(X+1):
        for j in range(Y+1):
            for k in range(Z+1):
                if (i+j+k)!=N :
                    mylist.append([i ,j ,k])


    print(mylist)

    return 0



if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    comprehension(x,y,z,n)


#!/bin/python3
# -*- coding: utf-8 -*-

#se ayth thn askhsh thelw boh8eia
#pernaei ola ta test cases mono kai mono epeidh ta eida kai eida oti mporei na
#exw mexri tria elaxista
#to problhma mou einai sthn for me to break 
#ean den balw to break mou bgazei error epeidh diagrafw stoixeio kai to mege8os ths 
#listas allazei mesa sto loop
#pws alliws ginetai ayto ?
#8elw dld na diagrapsw olh thn seira tou object pou exei thn timh ekeinh sthn deyterh 8esh

def findrunnersup(mylist):
    
    mingrade = min(mylist, key=lambda x: x[1])[1]
    
    for i in range(len(mylist)):
        if mylist[i][1] == mingrade:          
            mylist.pop(i)               
            break    
    for i in range(len(mylist)):
        if mylist[i][1] == mingrade:          
            mylist.pop(i)               
            break  
    for i in range(len(mylist)):
        if mylist[i][1] == mingrade:          
            mylist.pop(i)               
            break  
    
    runnergrade = min(mylist, key=lambda x: x[1])[1]    
    names = []    
    for i in range(len(mylist)):
        if mylist[i][1] == runnergrade:            
            names.append([mylist[i][0]])
            
    
    
    names = sorted(names)    
    flattened = [val for sublist in names for val in sublist]    
    print ('\n'.join(flattened))    

    return 0

if __name__ == '__main__':

    mylist = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        mylist.append([name , score])
        
    findrunnersup(mylist)
        


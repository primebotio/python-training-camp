#!/bin/python3
# -*- coding: utf-8 -*-

def parser(command_name, integers, mylist):
    if command_name == "insert":
        mylist.insert(integers[0], integers[1])
    elif command_name == "print":
        print(mylist)
    elif command_name == "remove":
        mylist.remove(integers[0])
    elif command_name == "append":
        mylist.append(integers[0])
    elif command_name == "sort":
        mylist.sort()
    elif command_name == "pop":
        mylist.pop()
    else:
        mylist.reverse()

    return 0

if __name__ == '__main__':
    N = int(input())
    mylist = []
    for i in range(N):
        full_command = input().split()
        command_name, integers = full_command[0], full_command[1:]
        integers = list(map(int, integers))
        parser(command_name,integers,mylist)









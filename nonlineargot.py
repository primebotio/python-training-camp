#!/bin/python3

import math
import os

#maximum number of characters in the string according to hackerrank
NO_OF_CHARS = 100000

# Complete the gameOfThrones function below.
def gameOfThrones(s):
    #create countermatrix full of zeros
    count = [0]*(NO_OF_CHARS)

    #count character occurences
    for i in range(len(s)):
        count[ord(s[i])] = count[ord(s[i])] + 1

    #count odd occuring characters
    odd = 0
    for i in range(NO_OF_CHARS):
        if (count[i]&1):
            odd += 1
        if odd>1 :
            return "NO"


    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()




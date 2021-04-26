#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# Complete the solve function below.
def solve(s):
    newString = ""
    
    for i in range(len(s)):
        if i == 0 and s[i].isalpha():
            newString += s[i].upper()
            
        elif s[i - 1] == " " and s[i].isalpha():
            newString += s[i].upper()
        
        else:
            newString += s[i]
    return newString

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)
    print(result)

    # fptr.write(result + '\n')

    # fptr.close()

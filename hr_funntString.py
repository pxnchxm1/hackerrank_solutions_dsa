'''
FUNNY STRING
..................................................................................
Determine whether a give string is funny. If it is, return Funny, otherwise return Not Funny.

'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    # Write your code here
    os,rs=[],[]
    for i,l in zip(s[:],s[-1::-1]):
        os.append(ord(i))
        rs.append(ord(l))
    for i in range(1,len(rs)):
       if (abs(os[i]-os[i-1])!=abs(rs[i]-rs[i-1])):
           return "Not Funny"
    return "Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()

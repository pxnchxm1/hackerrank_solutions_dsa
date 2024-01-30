'''
MINIMUM DISTANCE
-----------------------
The distance between two array values is the number of indices between them. Given a, 
find the minimum distance between any pair of equal elements in the array. If no such value exists, return -1.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Write your code here
    d = {}
    arr=[]
    for i in range(len(a)):
        if a[i] not in d:
            d[a[i]]=i
        else:
            arr.append(abs(d[a[i]]-i))
    return min(arr) if arr else -1
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()

'''
PICKING NUMBERS
........................................................................
Given an array of integers, find the longest subarray where the absolute
 difference between any two elements is less than or equal to .
 ........................................................................
'''
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    d = Counter(a)
    best = 0
    n = (len(a)*(len(a)+1)) // 2  #possible subarray count
    for i in range(n):
        best = max(d[i] + d[i+1], best)
    return best

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()

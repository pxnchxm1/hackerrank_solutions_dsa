#SUBARRAY DIVISION_________HACKERRANK
#..........................................................................
# Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.

# Lily decides to share a contiguous segment of the bar selected such that:

# The length of the segment matches Ron's birth month, and,
# The sum of the integers on the squares is equal to his birth day.
# Determine how many ways she can divide the chocolate.
#.....................................................................................
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    d_count=0
    l_count=0
    idx=0
    i=0
    count=0
    while i!=len(s):
        d_count+=s[i]
        l_count+=1
        if d_count==d and l_count==m:
            count+=1
            d_count,l_count=0,0
            idx+=1
            i=idx-1
        if d_count>d or l_count>m:
            d_count,l_count=0,0
            idx+=1
            i=idx-1

        i+=1
    return count
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()

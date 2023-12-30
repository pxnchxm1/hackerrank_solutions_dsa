'''
HACKERRANK     -  MAGIC SQUARE(3X3)
............................................................................................
We define a magic square to be an  matrix of distinct positive integers from  to  
where the sum of any row, column, or diagonal of length  is always equal to the same number:
the magic constant.You will be given a  matrix  of integers in the inclusive range .
We can convert any digit  to any other digit  in the range  at cost of . 
Given , convert it into a magic square at minimal cost. Print this cost on a new line.
Note: The resulting magic square must contain distinct integers in the inclusive range .
.........................................................................................................
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    # Write your code here
    s1 = s[0]+s[1]+s[2]
    comb = [[8,1,6,3,5,7,4,9,2],[6,1,8,7,5,3,2,9,4],
           [4,9,2,3,5,7,8,1,6],[2,9,4,7,5,3,6,1,8],
           [8,3,4,1,5,9,6,7,2],[4,3,8,9,5,1,2,7,6],
           [6,7,2,1,5,9,8,3,4],[2,7,6,9,5,1,4,3,8]]
    cost = float('inf')
    i=0
    while i!=8:
        dif=0
        for j,l in zip(comb[i],s1): 
            dif+=abs(j-l)
        if dif<cost: 
            cost=dif
        i+=1
    return cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()

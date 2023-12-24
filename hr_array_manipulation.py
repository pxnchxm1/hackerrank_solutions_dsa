# Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in the array.

# Example
# Queries are interpreted as follows:

#     a b k
#     1 5 3
#     4 8 7
#     6 9 1
# Add the values of  between the indices  and  inclusive:

# index->	 1 2 3  4  5 6 7 8 9 10
# 	[0,0,0, 0, 0,0,0,0,0, 0]
# 	[3,3,3, 3, 3,0,0,0,0, 0]
# 	[3,3,3,10,10,7,7,7,0, 0]
# 	[3,3,3,10,10,8,8,8,1, 0]
# The largest value is  after all operations are performed.

# Function Description

# Complete the function arrayManipulation in the editor below.

# arrayManipulation has the following parameters:

# int n - the number of elements in the array
# int queries[q][3] - a two dimensional array of queries where each queries[i] contains three integers, a, b, and k.
# Returns

# int - the maximum value in the resultant array
# Input Format

# The first line contains two space-separated integers  and , the size of the array and the number of operations.
# Each of the next  lines contains three space-separated integers ,  and , the left index, right index and summand.
#........................................................................................................................
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    arr=[0] * (n+1)
    for a,b,k in queries:
        arr[a-1]+=k
        if b<=n:
            arr[b]-=k
    mx =0
    curr=0
    for i in arr:
        curr+=i
        if curr>mx: mx=curr
    return mx

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

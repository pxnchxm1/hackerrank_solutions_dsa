''' SHERLOCK AND SQUARES
.............................................................
Watson likes to challenge Sherlock's math ability. 
He will provide a starting and ending value that describe a range of integers, 
inclusive of the endpoints. Sherlock must determine the number of square integers within that range.
Note: A square integer is an integer which is the square of an integer, eg:1,4,9,16....
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def squares(a, b):
    # Write your code here
    return len(range(math.ceil(math.sqrt(a)),int(math.sqrt(b))+1))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()

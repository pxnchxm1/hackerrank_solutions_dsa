'''
ENCRYPTION
...........................
An English text needs to be encrypted using the following encryption scheme.
First, the spaces are removed from the text. Let  be the length of this text.
Then, characters are written into a grid, whose rows and columns have the following constraints:

Example
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    sentence=s.replace(" ","")
    r=math.floor(len(sentence) ** (0.5))
    c=math.ceil(len(sentence) ** (0.5))
    x=""
    j=0
    while j<c:
        for i in range(j,len(sentence),c): x+=sentence[i]
        x+=" "
        j+=1
    
    return x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()

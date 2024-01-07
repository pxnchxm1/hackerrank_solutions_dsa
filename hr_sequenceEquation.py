
'''
SEQUENCE EQUATION
........................................................
Given a sequence of  integers,  where each element is distinct and satisfies . 
For each  where , that is  increments from  to , find any integer  such that  and keep a 
history of the values of  in a return array.
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(p):
    # Write your code here
    ans=[]
    p.insert(0,0)
    for i in range(n+1):
        y = p.index(p.index(i))
        if p[p[y]]==i:
            ans.append(y)
    ans.pop(0)
    return ans  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

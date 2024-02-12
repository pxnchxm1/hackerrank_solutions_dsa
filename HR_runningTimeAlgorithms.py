'''
RUNNING TIME OF ALGORITHMS
-------------------------------------------------------------------
In a previous challenge you implemented the Insertion Sort algorithm. 
It is a simple sorting algorithm that works well with small or mostly sorted data. However, it takes a long time to sort large unsorted data. To see why, we will analyze its running time.

Running Time of Algorithms
The running time of an algorithm for a specific input depends on the number of 
operations executed. The greater the number of operations, the longer the running time of an algorithm. We usually want to know how many operations an algorithm will execute in proportion to the size of its input, which we will call .

What is the ratio of the running time of Insertion Sort to the size of the input?
 To answer this question, we need to examine the algorithm.

Analysis of Insertion Sort
For each element  in an array of  numbers, Insertion Sort compares the number to
 those to its left until it reaches a lower value element or the start. At that point it shifts everything to the right up one and inserts  into the array.

How long does all that shifting take?

In the best case, where the array was already sorted, no element will need to be moved, so the algorithm will just run through the array once and return the sorted array. The running time would be directly proportional to the size of the input, so we can say it will take  time.'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'runningTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def runningTime(arr):
    count=0
    if len(arr)<=1 or arr==sorted(arr):
        return 0
    for i in range(1,len(arr)):
        x=arr[i]
        j=i-1
        while j >= 0 and x < arr[j]:  
            arr[j+1] = arr[j]  
            count+=1
            j -= 1
        arr[j+1] = x
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

'''
FLATLAND SPACE STATIONS
////////////////////////////////////////
Discussions	Editorial
Flatland is a country with a number of cities, 
some of which have space stations. Cities are numbered consecutively and each 
has a road of  length connecting it to the next city. It is not a circular route, 
so the first city doesn't connect with the last city. Determine the maximum distance 
from any city to its nearest space station.
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    ans = 0
    c.sort()
    for i in range(1,len(c)):
        ans = max(ans,(c[i]-c[i-1])//2)
    ans = max(ans,c[0],n-1-c[-1])
    return ans
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()

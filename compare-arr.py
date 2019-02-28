#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice=0
    bob=0
    list = []
    for i in range(len(a)) :
        for j in range(len(b)):
            if i==j:
                if a[i] > b[j]:
                    alice = alice + 1
                elif a < b:
                    bob = bob +1

    print ("alice is", alice)
    print ("bob is", bob)
    list.append(alice)
    list.append(bob)
    print (list)
    return list


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

   # fptr.write(' '.join(map(str, result)))
   # fptr.write('\n')

  #  fptr.close()

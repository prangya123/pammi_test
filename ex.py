
# array = []
# inp=input().split()
# for i in inp:
# 	array.append(int(i))
#
# print(array)

number_array = list()
number = input("Enter the number of elements you want:")
print ('Enter numbers in array: ')
for i in range(int(number)):
    n = input("number :")
    number_array.append(int(n))
print ('ARRAY: ',number_array)

k =

# number_array = set(number_array)
# print(number_array)
# print(sorted(number_array)[-2])

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the findNumber function below.
def findNumber(arr, k):
    if k in arr:
        x = "YES"
    else:
        x = "NO"
    return x


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    k = int(input().strip())

    res = findNumber(arr, k)

    fptr.write(res + '\n')

    fptr.close()


#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the oddNumbers function below.
def oddNumbers(l, r):
    list = []
    for i in range(l, r+1):
        if i % 2 != 0:
            list.append(i)
    return list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    r = int(input().strip())

    res = oddNumbers(l, r)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

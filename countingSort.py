#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def createArray(n):
    newArr=[]
    for x in range(n):
        newArr.append(0)
    return newArr

# def printf(arr):
#     for x in range(len(arr)):
#         print(arr[x], end=" ")
#     print("\n", end="")

def countingSort(arr):
    # Write your code here
    newArr=createArray(100)
    for x in range(len(arr)):
        newArr[arr[x]] += 1
    return newArr
    # printf(newArr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

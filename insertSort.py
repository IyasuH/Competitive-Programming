#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#


def printf(arr):
    for x in range(len(arr)):
        print(arr[x], end=" ")
    print("\n", end="")

def insertionSort1(n, arr):
    # Write your code here
    ini = n-1
    for x in range(n):
        civ  = arr[ini]
        # n-=1
        # print(arr[-(x+1)])
        if civ < arr[-(x+1)]:
            temp = arr[ini]
            arr[ini] = arr[-(x+1)]
            printf(arr)
            arr[-(x+1)] = temp
            ini-=1
    printf(arr)
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

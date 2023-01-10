#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#
def swap(arr, a, b):
    # just swap arr[a] and arr[b] and return the array
    temp=arr[a]
    arr[a]=arr[b]
    arr[b]=temp
    return arr

def countSwaps(a):
    swaps=0
    for i in range(len(a)):
        for j in range(len(a)-1):
            # // Swap adjacent elements if they are in decreasing order
            if (a[j] > a[j + 1]):
                swaps+=1
                a=swap(a,j, j + 1)
    print("Array is sorted in {} swaps.".format(swaps))
    print("First Element:", a[0])
    print("Last Element:", a[-1])
    return swaps

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
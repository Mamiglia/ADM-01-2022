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
def insertionSort1(n, arr):
    el = arr[-1]
    for i in range(len(arr)-2,-1, -1):
        if el < arr[i]:
            arr[i+1] = arr[i]
        else:
            arr[i+1] = el
            break
        print(" ".join(list(map(str,arr))))
    else:
        arr[0] = el
    print(" ".join(list(map(str,arr))))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

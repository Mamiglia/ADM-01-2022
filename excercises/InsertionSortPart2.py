#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    for i in range(1,len(arr)):
        if arr[i] > arr[i-1]:
            print(" ".join(list(map(str, arr))))
            continue
        for j in range(i-1, -1, -1):
            if arr[j] < arr[i]:
                arr.insert(j+1, arr.pop(i))
                break
        else:
            arr.insert(0, arr.pop(i))
        print(" ".join(list(map(str, arr))))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)

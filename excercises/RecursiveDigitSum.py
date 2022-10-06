#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
def superDigit(n, k):
    digits = map(int, list(str(n)))
    superdigit = sum(digits)
    print(superdigit)
    if superdigit * k < 10 :
        return superdigit * k
    elif superdigit < 10 :
        return superDigit(int(str(superdigit)*k), 1)
    return superDigit(superdigit, k)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

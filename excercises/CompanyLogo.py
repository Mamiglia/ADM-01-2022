#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = list(input())
    s.sort()
    C = Counter(s)
    print("\n".join(map(lambda t: f"{t[0]} {t[1]}", C.most_common(3))))
    
    

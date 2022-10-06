import re

T = int(input())
for _ in range(T):
    s = input()
    print(bool(re.match(r"[+-]?\d*\.\d+$", s)))

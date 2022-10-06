# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N = int(input())

for _ in range(N):
    num = input()
    res = bool(re.match(r'\w+ <[a-zA-Z][\w\.\-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>$', num))
    if res:
        print(num)

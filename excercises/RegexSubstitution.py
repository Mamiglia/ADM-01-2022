# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

N = int(input())
def sub(s):
    s = s[0]
    # print(s)
    if s==' ||':
        return ' or'
    elif s==' &&':
        return' and'
    
for _ in range(N):
    print(re.sub(r" (\|\||&&)(?= )", sub, input()))

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

S = input()
k = input()

i=0
while i < len(S):
    m = re.search(k, S[i:])
    if m is None:
        break
    print((m.start()+i, m.end()+i-1))
    i += 1 + m.start()

if i == 0:
    print((-1,-1))

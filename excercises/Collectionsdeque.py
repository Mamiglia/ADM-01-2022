from collections import deque

D = deque()
N = int(input())
for _ in range(N):
    cmd, *arg = input().split()
    getattr(D, cmd)(*arg)
    
print(" ".join(D))
    

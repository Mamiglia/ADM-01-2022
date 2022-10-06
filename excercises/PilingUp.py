from collections import deque
T = int(input())

for _ in range(T):
    n = int(input())
    cubes = deque(map(int, input().split()))
    
    curr = float('inf')
    for _ in range(n):
        if cubes[0] > cubes[-1]:
            v = cubes.popleft()
        else:
            v = cubes.pop()
        # print(v)
        if v > curr:
            print('No')
            break
        else:
            curr = v
    else: 
        print('Yes')
        
        

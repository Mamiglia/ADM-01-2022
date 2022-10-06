from collections import OrderedDict

B = OrderedDict()
N = int(input())

for _ in range(N):
    w = input()
    if w not in B:
        B[w] = 0
    B[w] += 1
    
print(len(B))
print(" ".join(map(str, B.values())))

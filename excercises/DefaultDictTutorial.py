from collections import defaultdict as ddict

n,m = map(int, input().split())
A = ddict(list)

for i in range(n):
    w = input()
    A[w].append(i+1)
for j in range(m):
    w = input()
    print(" ".join(map(str,A[w])) if len(A[w])>0 else '-1')


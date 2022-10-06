from collections import Counter

X = int(input())
x = Counter(map(int, input().split()))
N = int(input())
gain = 0

for _ in range(N):
    size, price = map(int, input().split())
    if x[size] > 0:
        x[size]-=1
        gain += price
        
print(gain)
    

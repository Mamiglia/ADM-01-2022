from collections import OrderedDict

B = OrderedDict()
N = int(input())
for _ in range(N):
    *item, price = input().split()
    price = int(price)
    item = " ".join(item)
    if item not in B:
        B[item] = 0
    B[item] += price
    
for k in B:
    print(k,B[k])
    

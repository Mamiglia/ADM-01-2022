# Enter your code here. Read input from STDIN. Print output to STDOUT
A =  set(map(int, input().split()))
n = int(input())

for _ in range(0,n):
    s = set(map(int, input().split()))
    if len(A)<=len(s) or not A.issuperset(s):
        print(False)
        break
else:
    print(True)
        
    

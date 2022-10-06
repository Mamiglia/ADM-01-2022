a_size = int(input())
A = set(map(int, input().split(" ")))
N = int(input())

for _ in range(N):
    cmd = input().split()[0]
    s = set(map(int, input().split(" ")))
    getattr(A, cmd)(s)
    
print(sum(A))

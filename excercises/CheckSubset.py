# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())

for _ in range(T):
    input()
    A = set(map(int, input().split(" ")))
    input()
    B = set(map(int, input().split(" ")))
    print(A.issubset(B))

# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
arr = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
happy = 0

for a in arr:
    happy += a in A
    happy -= a in B
print(happy)

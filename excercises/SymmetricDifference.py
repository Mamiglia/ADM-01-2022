# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
m = set(map(int, input().split(" ")))
N = int(input())
n = set(map(int, input().split(" ")))

symm_diff = list(m.difference(n).union(n.difference(m)))
symm_diff.sort()
for n in symm_diff:
    print(n)

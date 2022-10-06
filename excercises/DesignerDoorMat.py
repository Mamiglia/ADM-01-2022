# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M= map(int,input().split())

for i in range(N//2):
    print(('.' + '|..|..'*i + '|.').center(M,'-'))

print('WELCOME'.center(M,'-'))

for i in range(N//2):
    print(('.' + '|..|..'*(N//2 - i - 1) + '|.').center(M,'-'))

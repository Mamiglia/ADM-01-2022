# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N = int(input())

for _ in range(N):
    num = input()
    res = bool(re.match(r'[789]\d{9}$', num))
    print('YES' if res else 'NO')

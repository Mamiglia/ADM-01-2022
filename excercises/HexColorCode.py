# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N = int(input())

for _ in range(N):
    num = input()
    res = re.findall(r'(#[0-9a-f]{6}|#[0-9a-f]{3})(?! *{?$)', num, re.IGNORECASE)
    if res != []:
        print("\n".join(res))

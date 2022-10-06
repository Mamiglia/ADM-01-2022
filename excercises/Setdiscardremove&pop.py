n = int(input())
s = set(map(int, input().split()))

N = int(input())
for _ in range(N):
    cmd = input()
    if 'pop' in cmd:
        s.pop()
    elif 'remove' in cmd:
        o = int(cmd.split()[1])
        if o in s:
            s.remove(o)
    elif 'discard' in cmd:
        o = int(cmd.split()[1])
        s.discard(o)
print(sum(s))

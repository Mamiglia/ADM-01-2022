import re

N = int(input())
pattern = r'^(?=(?:(\d)-?(?!(?:-?\1){3}))*$)([456]\d\d\d)(-?\d\d\d\d){3}$'
for _ in range(N):
    if re.match(pattern, input()):
        print("Valid")
    else:
        print("Invalid")

import re

N = int(input())
pattern = r'^(?=.*[A-Z].*[A-Z])(?=.*\d.*\d.*\d)(?:([a-zA-Z\d])(?!.*\1)){10}$'
for _ in range(N):
    if re.match(pattern, input()):
        print("Valid")
    else:
        print("Invalid")

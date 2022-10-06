from collections import OrderedDict as Odict

S = input()
D = Odict()
D['lower'] = []
D['upper'] = []
D['odd'] = []
D['even'] = []
for c in S:
    if c.islower():
        D['lower'].append(c)
    elif c.isupper():
        D['upper'].append(c)
    elif int(c) % 2 == 0:
        D['even'].append(c)
    elif int(c)%2!=0:
        D['odd'].append(c)
    else:
        print("UNEXPECTED")

R = []
for k in D:
    D[k].sort()
    R += D[k]

print("".join(R))

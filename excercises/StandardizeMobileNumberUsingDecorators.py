import re

def wrapper(f):
    def fun(l):
        r = []
        for n in l:
            n = re.sub(r'^(?:\+91|91|0)?(\d{5})(\d{5})$', r'+91 \1 \2', n)
            r.append(n)
        return f(r)
    return fun


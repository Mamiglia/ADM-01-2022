from math import log2

def print_formatted(number):
    t = int(log2(number)+1)
    form = f'{{n:{t}}} {{n:{t}o}} {{n:{t}X}} {{n:{t}b}}'
    for n in range(1,number+1):
        print(form.format(n=n))



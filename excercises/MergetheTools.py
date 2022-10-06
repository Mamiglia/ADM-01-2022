def merge_the_tools(string, k):
    for t in [string[i:i+k] for i in range(0,len(string)-k+1,k)]:
        u = ''
        for c in t:
            if c not in u:
                u += c
        print(u)


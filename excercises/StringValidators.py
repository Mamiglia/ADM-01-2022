def check(func, s):
    for c in s:
        if func(c):
            print(True)
            break
    else:
        print(False)

if __name__ == '__main__':
    s = input()
    tests = [str.isalnum, str.isalpha, str.isdigit,  str.islower, str.isupper]
    for f in tests:
        check(f, s)

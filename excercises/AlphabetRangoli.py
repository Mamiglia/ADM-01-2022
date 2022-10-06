def print_rangoli(size):
    if (size==1):
        print('a')
        return
    letters = [chr(ord('a') + i) for i in range(size)]
    lines = [letters[size:i:-1] + letters[i:size] for i in range(size-1,-1,-1)]
    for it in lines[size-2::-1]:
        lines.append(it)
    width = len(lines[size-1])*2 - 1
    for it in lines:
        print("-".join(it).center(width,'-'))


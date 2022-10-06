VOWELS = ['A','E','I', 'O', 'U']

def minion_game(string):
    vow = 0 #Kevin
    cons = 0 #Stuart
    for i in range(len(string)):
        if string[i] in VOWELS:
            vow += len(string) - i
        else:
            cons += len(string) - i
    if vow == cons:
        print(f"Draw")
    elif vow>cons:
        print(f"Kevin {vow}")
    else:
        print(f"Stuart {cons}")



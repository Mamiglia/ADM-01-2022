if __name__ == '__main__':
    m = dict()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in m.keys():
            m[score].append(name)
        else:
            m[score] = [name]
    scores = list(m.keys())
    scores.sort()
    m[scores[1]].sort()
    for name in m[scores[1]]:
        print(name)
        
            
        
        

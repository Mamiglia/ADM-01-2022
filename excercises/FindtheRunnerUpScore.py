if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    best = -101
    runner_up = -101
    for i in arr:
        if i>best:
            runner_up=best
            best = i
        elif i>runner_up and i<best:
            runner_up = i
    print(runner_up)
            
            

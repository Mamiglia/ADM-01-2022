T = int(input())

for _ in range(T):
    try:     
        a, b = input().split()
        print(int(a)//int(b))
    except Exception as e:
        print("Error Code:", e)
        
        
        

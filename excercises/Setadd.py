# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
countries = set()

for _ in range(N):
    countries.add(input())
    
print(len(countries))

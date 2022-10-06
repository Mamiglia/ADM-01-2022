# Enter your code here. Read input from STDIN. Print output to STDOUTN
N, X = map(int, input().split())

marks_table = []
for _ in range(X):
    marks_table.append(list(map(float, input().split())))
    
# print(zip(*marks_table))
avgs = [sum(x)/X for x in list(zip(*marks_table))]
for x in avgs:
    print(f"{x:.1f}")
# print("\n".join(map(lambda x : str(sum(x)), zip(*marks_table))))

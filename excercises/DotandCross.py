import numpy

N = int(input())

a = []
for _ in range(N):
    a.append(list(map(int, input().split())))
A = numpy.array(a)

b = []
for _ in range(N):
    b.append(list(map(int, input().split())))
B = numpy.array(b)
print(numpy.dot(A,B))

 

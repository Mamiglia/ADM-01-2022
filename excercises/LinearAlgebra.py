import numpy

N = int(input())

a = []
for _ in range(N):
    a.append(list(map(float, input().split())))
A = numpy.array(a)

print(round(numpy.linalg.det(A), 2))

import numpy

N,M = list(map(int, input().split()))

a = []
for _ in range(N):
    a.append(list(map(int, input().split())))
A = numpy.array(a)

print(numpy.max(numpy.min(A, axis=1)))

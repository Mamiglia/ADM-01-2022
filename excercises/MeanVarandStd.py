import numpy
# numpy.set_printoptions(sign=' ')

N,M = list(map(int, input().split()))

a = []
for _ in range(N):
    a.append(list(map(int, input().split())))
A = numpy.array(a)

print(numpy.mean(A, axis=1))
print(numpy.var(A, axis=0))
print(round(numpy.std(A, axis=None),11))

import numpy
N, M = list(map(int, input().split()))
m = [list(map(int, input().split())) for _ in range(N)]
m = numpy.array(m)
print(m.T)
print(m.flatten())

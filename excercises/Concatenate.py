import numpy

N, M, P = list(map(int, input().split()))

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
arr = numpy.array(arr)
    
brr = []
for _ in range(M):
    brr.append(list(map(int, input().split())))
brr = numpy.array(brr)

print(numpy.concatenate((arr, brr)))

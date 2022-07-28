import sys

n = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))

count = {}

for i in arr1:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for j in arr2:
    if j in count:
        print(count[j], end = ' ')
    else:
        print(0, end = ' ')

import sys

n = int(sys.stdin.readline())
A = set(map(int, sys.stdin.readline().split()))

m = int(input())
B = list(map(int, sys.stdin.readline().split()))

for i in B:
    if i in A:
        print(1)
    else:
        print(0)
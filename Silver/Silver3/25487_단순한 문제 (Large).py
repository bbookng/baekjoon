import sys

T = int(sys.stdin.readline())
for _ in range(T):
    print(min(list(map(int, sys.stdin.readline().split()))))


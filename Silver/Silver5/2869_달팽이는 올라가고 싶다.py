import sys

a, b, v = map(int, sys.stdin.readline().split())

count = (v-b) % (a-b)
result = (v-b) // (a-b)
if count == 0:
    print(result)
else:
    print(result + 1)

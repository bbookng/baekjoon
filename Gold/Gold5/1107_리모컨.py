import sys
input = lambda : sys.stdin.readline().strip()

N = int(input())
M = int(input())
arr = set(input().split())
result = abs(N-100)

for i in range(10000001):
    i = str(i)
    for j in range(len(i)):
        if i[j] in arr:
            break
    else:
        result = min(result, len(i) + abs(N - int(i)))


print(result)

# import sys
# input = lambda : sys.stdin.readline().strip()
#
# N = int(input())
# M = int(input())
# arr = set(input().split())
# result = abs(N-100)
#
#
#
# print(result)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr1 = []
arr2 = []

for i in range(N+M):
    if i < N:
        arr1.append(input().rstrip())
    else:
        arr2.append(input().rstrip())

result = sorted(list(set(arr1) & set(arr2)))
print(len(result))
for i in result:
    print(i)

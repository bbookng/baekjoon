import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

S = int(input())
for i in range(S):
    sex, num = map(int, input().split())
    if sex == 1:
        for j in range(N):
            if (j+1) % num == 0:
                if arr[j] == 0:
                    arr[j] = 1
                else:
                    arr[j] = 0
    else:
        num -= 1
        for j in range(N):
            if num-j >= 0 and num+j < N and arr[num-j] == arr[num+j]:
                if arr[num-j] == 1:
                    arr[num-j] = arr[num+j] = 0
                else:
                    arr[num-j] = arr[num+j] = 1
            else:
                break

for i in range(N):
    print(arr[i], end = ' ')
    if (i+1) % 20 == 0:
        print()

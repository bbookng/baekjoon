import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
arr = [list(input()) for _ in range(n)]

result = []

def solution(arr):
    K = len(arr)
    if K == 1:
        return arr[0][0]

    arr1 = [arr[i][:K//2] for i in range(K//2)]
    arr2 = [arr[i][K//2:] for i in range(K//2)]
    arr3 = [arr[i][:K//2] for i in range(K//2,K)]
    arr4 = [arr[i][K//2:] for i in range(K//2,K)]

    s1 = solution(arr1)
    s2 = solution(arr2)
    s3 = solution(arr3)
    s4 = solution(arr4)

    if s1 == s2 == s3 == s4:
        result.append(s1)

    else:
        result.append('(')
        for s in [s1, s2, s3, s4]:
            result.append(s)
        result.append(')')

solution(arr)
print(*result, end='')


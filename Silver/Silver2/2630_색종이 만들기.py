import sys
input = lambda :sys.stdin.readline().strip()

result = [0, 0, 0]

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
        return s1

    else:
        for s in [s1, s2, s3, s4]:
            result[s] += 1

    return 2





N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
solution(arr)
if result == [0, 0, 0]:
    result[arr[0][0]] += 1
print(result[0])
print(result[1])
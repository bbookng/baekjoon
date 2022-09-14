import sys
input = lambda: sys.stdin.readline().strip()

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

result = [0, 0, 0]

def solution(arr):

    K = len(arr)
    if K == 1:
        return arr[0][0]

    arr1 = [arr[i][:K//3] for i in range(K//3)]
    arr2 = [arr[i][:K//3] for i in range(K//3*2, K)]
    arr3 = [arr[i][:K//3] for i in range(K//3, K//3*2)]
    arr4 = [arr[i][K//3*2:] for i in range(K//3)]
    arr5 = [arr[i][K//3*2:] for i in range(K//3*2, K)]
    arr6 = [arr[i][K//3*2:] for i in range(K//3, K//3*2)]
    arr7 = [arr[i][K//3:K//3*2] for i in range(K//3)]
    arr8 = [arr[i][K//3:K//3*2] for i in range(K//3*2, K)]
    arr9 = [arr[i][K//3:K//3*2] for i in range(K//3, K//3*2)]

    s1 = solution(arr1)
    s2 = solution(arr2)
    s3 = solution(arr3)
    s4 = solution(arr4)
    s5 = solution(arr5)
    s6 = solution(arr6)
    s7 = solution(arr7)
    s8 = solution(arr8)
    s9 = solution(arr9)

    if s1 == s2 == s3 == s4 == s5 == s6 == s7 == s8 == s9:
        return s1


    else:
        for s in [s1, s2, s3, s4, s5, s6, s7, s8, s9]:
            if s == -1:
                result[0] += 1
            elif s == 0:
                result[1] += 1
            elif s == 1:
                result[2] += 1

solution(arr)

for i in result:
    print(i)

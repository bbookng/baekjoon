N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

tmp = []
result = []

def solution(n):
    if n == M:
        s = ' '.join(map(str, tmp))
        if s not in result:
            print(s)
            result.append(s)
        return
    else:
        for i in range(len(arr)):
            if n == 0 or tmp[-1] <= arr[i]:
                tmp.append(arr[i])
                solution(n+1)
                tmp.pop()

solution(0)
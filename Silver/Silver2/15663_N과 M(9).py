N, M = map(int,input().split())
numbers = list(map(int, input().split()))
numbers.sort()

check = set()
chosen = [-1] * M
visited = [0] * N

def solution(i, M):
    if i == M:
        print(" ".join(map(str, chosen)))
        check.add(tuple(chosen))
        return

    for j in range(len(numbers)):
        for k in range(M):
            if numbers[j] not in chosen:
                chosen[k] = numbers[j]
                visited[j] = 1
                solution(i+1, M)
                visited[j] = 0




solution(0, M)
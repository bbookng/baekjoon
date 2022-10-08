import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(now):
    global result
    visited[now] = 1
    cycle.append(now)

    if visited[arr[now]]:
        if arr[now] in cycle:
            result += cycle[cycle.index(arr[now]):]
        return
    else:
        dfs(arr[now])


T = int(input())
for _ in range(T):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [0] * (n+1)

    result = []

    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(n - len(result))

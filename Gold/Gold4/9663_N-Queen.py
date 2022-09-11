def check(x):
    for i in range(x):
        if col[x] == col[i] or abs(col[i]-col[x]) == x-i:
            return False
    return True

def dfs(x):
    global result
    if x == N:
        result += 1
        return
    for i in range(N):
        col[x] = i
        if check(x):
            dfs(x+1)

N = int(input())
result = 0
col = [0] * 15

dfs(0)
print(result)

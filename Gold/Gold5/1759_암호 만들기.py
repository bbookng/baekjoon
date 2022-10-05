import sys
input = sys.stdin.readline

def dfs(cnt, idx):
    if cnt == L:
        mo, ja = 0, 0

        for i in range(L):
            if tmp[i] in ('a', 'e', 'i', 'o', 'u'):
                mo += 1
            else:
                ja += 1

        if mo >= 1 and ja >= 2:
            print(''.join(tmp))
        return

    for i in range(idx, C):
        tmp.append(alphabet[i])
        dfs(cnt + 1, i + 1)
        tmp.pop()


L, C = map(int, input().split())
alphabet = list(input().split())
alphabet.sort()
tmp = []
dfs(0, 0)


import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N = int(input())
    clothes = {}

    for _ in range(N):
        a, b = input().split()
        if clothes.get(b) == None:
            clothes[b] = set()
        clothes[b].add(a)

    cnt = 1
    for key in clothes.keys():
        cnt *= len(clothes[key]) + 1

    print(cnt-1)
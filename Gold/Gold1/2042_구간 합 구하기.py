import sys
input = sys.stdin.readline


def init(start, end, node):  # 세그먼트 트리 만들기
    if start == end:
        tree[node] = nList[start]
        return tree[node]

    mid = (start + end) // 2
    tree[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1)
    return tree[node]


# 구간 합 구하기
def summit(start, end, node, left, right):
    # left 와 right가 범위에서 벗어났기 떄문에 return
    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return tree[node]

    mid = (start+end) // 2
    return summit(start, mid, node*2, left, right) + summit(mid + 1, end, node*2+1, left, right)


# 특정 인덱스 값 바꾸기
def update(start, end, node, index, diff):
    if index < start or index > end:
        return

    tree[node] += diff
    if start == end:
        return

    mid = (start+end) // 2
    update(start, mid, node*2, index, diff)
    update(mid + 1, end, node * 2 + 1, index, diff)


n, m, k = map(int, input().split())
nList = []
tree = [0] * ((4 * n))

for i in range(n):
    nList.append(int(input()))

init(0, n - 1, 1)

for i in range(m + k):
    cmd = list(map(int, input().split()))

    if cmd[0] == 1:
        cmd[1] -= 1
        diff = cmd[2] - nList[cmd[1]]
        nList[cmd[1]] = cmd[2]
        update(0, n - 1, 1, cmd[1], diff)
    elif cmd[0] == 2:
        print(summit(0, n - 1, 1, cmd[1] - 1, cmd[2] - 1))
def solution(N, trees):
    trees.sort()
    std = trees[-1]
    while std in trees:
        trees.pop()

    trees = list(map(lambda x: std-x, trees))
    one, two = 0, 0
    for tree in trees:
        one += tree % 2
        two += tree // 2


    while one < two:
        one += 2
        two -= 1

    if one == two:
        return one*2
    elif one - two == 2:
        return one*2 - 2
    else:
        return one * 2 - 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    trees = list(map(int, input().split()))

    cnt = solution(N, trees)
    print(cnt)


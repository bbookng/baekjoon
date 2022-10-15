T = int(input())

for tc in range(1, T+1):
    N = int(input())
    trees = list(map(int, input().split()))

    trees.sort()
    std = trees[-1]
    flag = True
    cnt = 0

    while std in trees:
        trees.pop()

    while trees:
        for i in range(len(trees)):
            print(cnt, trees[i])
            if flag:
                if std-1 in trees:
                    cnt += 1
                    flag = False
                    trees.remove(std-1)
                    break
                trees[i] += 1
                flag = False
                cnt += 1
            else:
                if std-2 in trees:
                    cnt += 1
                    flag = True
                    trees.remove(std-2)
                    break
                trees[i] += 2
                if trees[i] > std:
                    trees[i] -= 2

                flag = True
                cnt += 1



        while std in trees:
            trees.pop()



    print(cnt)
import sys
input = sys.stdin.readline

for _ in range(4):
    arr = list(map(int, input().split()))
    sq1 = [arr[i] for i in range(4)]
    sq2 = [arr[i] for i in range(4, 8)]

    check = set(sq1) & set(sq2)

    if len(check):
        print('c') if len(check) > 1 else print('b')
    else:
        if sq1[0] <= sq2[0] <= sq1[2] or sq1[0] <= sq2[2] <= sq1[2]:
            print('a')
        elif sq1[1] <= sq2[1] <= sq1[3] or sq1[1] <= sq2[3] <= sq1[3]:
            print('a')
        else:
            print('d')


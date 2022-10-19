T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    i = 1
    result = 'no'
    while True:
        if i == A:
            break
        tmp = int(A // i)
        if tmp * i == A and tmp + i == B:
            result = 'yes'
            break
        else:
            i += 1
    print(result)
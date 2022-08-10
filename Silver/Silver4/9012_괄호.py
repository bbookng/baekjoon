t = int(input())

for i in range(t):
    arr = list(input())

    cnt1 = 0
    cnt2 = 0

    for j in arr:
        if j == '(':
            cnt1 += 1
        elif j == ')':
            cnt2 += 1

            if cnt1 < cnt2:
                break

    if cnt1 == cnt2:
        result = 'YES'
    else:
        result = 'NO'

    print(result)
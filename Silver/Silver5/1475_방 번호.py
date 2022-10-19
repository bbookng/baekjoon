N = list(map(int, input()))

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
cnt = 1

for i in range(len(N)):
    if N[i] == 6 or N[i] == 9:
        if 6 in numbers:
            numbers.remove(6)
        elif 9 in numbers:
            numbers.remove(9)
        else:
            numbers += [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            numbers.remove(N[i])
            cnt += 1
    else:
        if N[i] in numbers:
            numbers.remove(N[i])
        else:
            numbers += [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            numbers.remove(N[i])
            cnt += 1

print(cnt)
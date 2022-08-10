S = input()

for i in range(ord('a'), ord('z')+1):
    if chr(i) in S:
        print(S.index(chr(i)), end=" ")
    else:
        print(-1, end = " ")
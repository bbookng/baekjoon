A, B = map(int, input().split())
C = int(input())

B = B+C
while B > 59:
    A += 1
    if A > 23:
        A = 0
    B -= 60

print(A, B)
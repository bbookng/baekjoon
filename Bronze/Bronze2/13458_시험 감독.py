N = int(input())
arr = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = N
for i in arr:
    i -= B
    if i < 0:
        continue
    cnt += i // C if i % C == 0 else i // C + 1

print(cnt)


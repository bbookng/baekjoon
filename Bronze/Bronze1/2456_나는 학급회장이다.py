N = int(input())

candidates = [0, 0, 0]

for i in range(N):
    a, b, c = map(int, input().split())
    candidates[0] += a
    candidates[1] += b
    candidates[2] += c

max_ = max(candidates)

if candidates.count(max_) > 1:
    print(0, max_)
else:
    print(candidates.index(max_) + 1, max_)
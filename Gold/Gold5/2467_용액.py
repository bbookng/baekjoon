import sys
input = sys.stdin.readline

N = int(input())
fluid = list(map(int, input().split()))

left = 0
right = N - 1
min_ = int(2e9)
answer = (fluid[0], fluid[N-1])

while left < right:
    if abs(fluid[left] + fluid[right]) < min_:
        min_ = abs(fluid[left] + fluid[right])
        answer = (fluid[left], fluid[right])

    if abs(fluid[left]) < abs(fluid[right]):
        right -= 1
    else:
        left += 1

print(' '.join(map(str, answer)))

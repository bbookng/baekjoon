direction = ['N', 'E', 'S', 'W']

now = 0

for _ in range(10):
    order = int(input())
    if order == 1:
        now += 1
    elif order == 2:
        now += 2
    else:
        now -= 1

print(direction[now % 4])
import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())
board = [[0] * C for _ in range(R)]

shark = dict()
total = 0

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    shark[(r-1, c-1)] = (s, d, z)

def catch(col):
    global total
    for i in range(R):
        if (i, col) in shark:
            total += shark[(i, col)][2]
            print(i, col, total)
            shark.pop((i, col))
            break

def move():
    for k, v in list(shark.items()):
        x, y = k
        s, d, z = v

        if d == 1:
            d = 2 if ((y - s) // R) % 2 else 1
            y = R - ((y - s) % R)

        elif d == 2:
            d = 1 if ((y + s) // R) % 2 else 2
            y = R - ((y + s) % R)

        elif d == 3:
            d = 4 if ((x + s) // C) % 2 else 3
            x = R - ((x + s) % C)

        elif d == 4:
            d = 3 if ((x - s) // C) % 2 else 4
            x = R - ((x - s) % C)

        if (x, y) in shark:
            if shark[(x, y)][2] > z:
                continue
            else:
                shark.pop((x, y))
                shark[(x, y)] = (s, d, z)

for i in range(C):
    catch(i)
    move()
    print(shark)

print(total)

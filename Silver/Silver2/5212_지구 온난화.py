r, c = map(int, input().split())

island = [list(input()) for _ in range(r)]

# 변경할 위치를 저장할 리스트
to_change = []

for i in range(r):
    for j in range(c):
        if island[i][j] == 'X':
            cnt = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = i + dx, j + dy
                if 0 <= nx < r and 0 <= ny < c:
                    if island[nx][ny] == '.':
                        cnt += 1
                else:
                    cnt += 1
            if cnt >= 3:
                to_change.append((i, j))

# 저장된 위치를 한 번에 변경
for x, y in to_change:
    island[x][y] = '.'

# 섬('X')이 존재하는 최소 및 최대 행과 열 찾기
min_row, max_row = r, 0
min_col, max_col = c, 0

for i in range(r):
    for j in range(c):
        if island[i][j] == 'X':
            min_row = min(min_row, i)
            max_row = max(max_row, i)
            min_col = min(min_col, j)
            max_col = max(max_col, j)

# 섬이 모두 없어졌을 경우 대비
if min_row > max_row or min_col > max_col:
    print()
else:
    for i in range(min_row, max_row+1):
        print(''.join(island[i][min_col:max_col+1]))
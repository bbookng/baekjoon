from collections import deque


def reachTheEnd(grid, maxTime):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    n, m = len(grid), len(grid[0])
    visited = [[False] * m for _ in range(n)]

    q = deque([(0, 0, 0)])
    visited[0][0] = True

    while q:
        x, y, t = q.popleft()

        if x == n - 1 and y == m - 1:
            return "Yes" if t <= maxTime else "No"

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == '.' and t + 1 <= maxTime:
                visited[nx][ny] = True
                q.append((nx, ny, t + 1))

    return "No"


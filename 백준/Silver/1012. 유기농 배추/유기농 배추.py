from collections import deque

def bfs(a, b):
    q = deque()
    q.append([a, b])
    land[a][b] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if land[nx][ny] == 1:
                land[nx][ny] = 0
                q.append([nx, ny])

    return


T = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(T):
    cnt = 0
    m, n, k = map(int, input().split())
    land = [[0] * m for _ in range(n)]

    for i in range(k):
        x, y = map(int, input().split())
        land[y][x] = 1

    for a in range(n):
        for b in range(m):
            if land[a][b] == 1:
                bfs(a, b)
                cnt += 1

    print(cnt)

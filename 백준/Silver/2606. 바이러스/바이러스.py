from collections import deque
def bfs(v):
    visited[v] = 1
    q = deque()
    q.append(v)

    while q:
        x = q.popleft()
        for i in range(n + 1):
            if computer[i][x] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = 1


n = int(input())
m = int(input())
computer = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(m):
    x, y = map(int, input().split())
    computer[x][y] = computer[y][x] = 1

bfs(1)

print(sum(visited) - 1)
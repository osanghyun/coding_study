import collections


n, m, k = map(int, input().split())
graph = [[0]*m for _ in range(n)]

for _ in range(k):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 1

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(x, y):
    global graph
    graph[x][y] = 0
    queue = collections.deque()
    queue.append((x, y))
    ret: int = 1

    while queue:
        x, y = queue.popleft()

        for t in range(4):
            nx, ny = x + dx[t], y + dy[t]

            if -1 < nx < n and -1 < ny < m and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0
                ret += 1

    return ret


ans: int = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            ans = max(ans, bfs(i, j))

print(ans)

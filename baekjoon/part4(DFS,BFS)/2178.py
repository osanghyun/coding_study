import collections

n, m = map(int, input().split())

graph = [list(map(int, input().strip())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = collections.deque()

queue.append((0, 0))

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx, ny))

print(graph[n-1][m-1])

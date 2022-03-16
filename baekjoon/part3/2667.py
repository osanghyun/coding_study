n = int(input())

graph = [list(map(int, input().strip())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x: int, y: int):
    global graph, dx, dy

    if graph[x][y] == 0:
        return 0

    graph[x][y] = 0
    count = 1
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if -1 < nx < n and -1 < ny < n:
            count += dfs(nx, ny)
    return count


counts = []

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            counts.append(dfs(i, j))

print(len(counts))

counts.sort()

for i in range(len(counts)):
    print(counts[i])

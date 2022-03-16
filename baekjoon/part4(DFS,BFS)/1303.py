n, m = map(int, input().split())

graph = [list(input().strip()) for _ in range(m)]

w_power = 0
b_power = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def w_dfs(x: int, y: int) -> int:
    w_count = 0
    if graph[x][y] != 'W':
        return w_count
    else:
        w_count = 1
        graph[x][y] = '0'

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if -1 < nx < m and -1 < ny < n:
            w_count += w_dfs(nx, ny)

    return w_count


def b_dfs(x: int, y: int) -> int:
    b_count = 0
    if graph[x][y] != 'B':
        return b_count
    else:
        b_count = 1
        graph[x][y] = '0'

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if -1 < nx < m and -1 < ny < n:
            b_count += b_dfs(nx, ny)

    return b_count


for col in range(m):
    for row in range(n):
        if graph[col][row] == 'W':
            wp = w_dfs(col, row)
            w_power += wp * wp
        elif graph[col][row] == 'B':
            bp = b_dfs(col, row)
            b_power += bp * bp

print(w_power, b_power)

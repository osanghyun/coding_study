import collections


h, w = map(int, input().split())

graph = []

for idx in range(h):
    graph.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def count_cheese(data: [[]]) -> int:
    cheese_number: int = 0

    for r in data:
        cheese_number += r.count(1)

    return cheese_number


def melting_cheese(x, y):
    que = collections.deque()
    que.append((x, y))
    visited = [[True]*w for _ in range(h)]

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue
            if visited[nx][ny]:
                if graph[nx][ny] == 1:
                    temp[nx][ny] = 0
                else:
                    que.append((nx, ny))
                visited[nx][ny] = False


melting_time = 0
num_cheese = 0
temp = graph.copy()

while count_cheese(graph) != 0:

    num_cheese = count_cheese(graph)

    melting_cheese(0, 0)
    graph = temp.copy()

    melting_time += 1

print(melting_time)
print(num_cheese)

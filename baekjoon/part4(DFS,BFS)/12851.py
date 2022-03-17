import collections

subin, target = map(int, input().split())

visited = [[-1, 0] for _ in range(100001)]
visited[subin][0] = 0  # 최소 시간
visited[subin][1] = 1  # 도달 횟수

q = collections.deque([subin])

while q:
    loc = q.popleft()

    for x in [loc + 1, loc - 1, loc * 2]:
        if 0 <= x <= 100000:
            if visited[x][0] == -1:
                visited[x][0] = visited[loc][0] + 1
                visited[x][1] = visited[loc][1]
                q.append(x)
            elif visited[x][0] == visited[loc][0] + 1:
                visited[x][1] += visited[loc][1]

print(visited[target][0])
print(visited[target][1])

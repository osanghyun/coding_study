import collections

n, m, v = map(int, input().split())

d = collections.defaultdict(list)

dfs_path = [v]
bfs_path = [v]

for _ in range(m):
    v1, v2 = map(int, input().split())
    d[v1].append(v2)
    d[v1].sort()

    d[v2].append(v1)
    d[v2].sort()


def dfs(vertex: int):
    global n, m, v, d, dfs_path

    for ver in d[vertex]:
        if ver not in dfs_path:
            dfs_path.append(ver)
            dfs(ver)


def bfs(vertex: int):
    global n, m, v, d, bfs_path

    queue = collections.deque()
    queue.append(vertex)

    while queue:
        pop_ver = queue.popleft()
        for ver in d[pop_ver]:
            if ver not in bfs_path:
                queue.append(ver)
                bfs_path.append(ver)


dfs(v)
bfs(v)

for i in dfs_path:
    print(i, end=' ')
print()

for i in bfs_path:
    print(i, end=' ')

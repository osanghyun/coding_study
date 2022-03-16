import collections

com_count = int(input())  # 컴퓨터의 수

pair_count = int(input())  # 연결된 컴퓨터 쌍의 수

# 양방향 그래프 생성.
graph = collections.defaultdict(list)

for _ in range(pair_count):
    com1, com2 = map(int, input().split())
    graph[com1].append(com2)
    graph[com2].append(com1)

path = []


def dfs(com: int):
    global path
    for v in graph[com]:
        if v not in path:
            path.append(v)
            dfs(v)


dfs(1)
print(len(path)-1)

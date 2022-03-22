import collections
import heapq
import sys


input = sys.stdin.readline

node_num = int(input())

edge_num = int(input())

graph = collections.defaultdict(list)

for _ in range(edge_num):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

start_node, end_node = map(int, input().split())

Q = [(0, start_node)]
dist = collections.defaultdict(int)

ans: int = -1

while Q:
    cost, node = heapq.heappop(Q)

    if node == end_node:
        ans = cost
        break

    if node not in dist:
        dist[node] = cost
        for v, w in graph[node]:
            alt = cost + w
            heapq.heappush(Q, (alt, v))

print(ans)

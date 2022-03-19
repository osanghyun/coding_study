import heapq
import sys

input = sys.stdin.readline

n = int(input())

Q = []

ret = []

for _ in range(n):
    input_num = int(input())
    if input_num == 0:
        if len(Q) == 0:
            ret.append(0)
        else:
            ret.append(-heapq.heappop(Q))
    else:
        heapq.heappush(Q, -input_num)

for x in ret:
    print(x)

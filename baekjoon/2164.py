import collections

n = int(input())

q = collections.deque()

for x in range(1, n+1):
    q.append(x)

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())

print(q[0])

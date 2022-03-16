import collections

a, b = map(int, input().split())

queue = collections.deque([(a, 1)])

ans: int = -1

while queue:
    num, count = queue.popleft()

    if num == b:
        ans = count
        break

    if num * 2 <= b:
        queue.append((num * 2, count + 1))

    if (num * 10) + 1 <= b:
        queue.append((num * 10 + 1, count + 1))

print(ans)

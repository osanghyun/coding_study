n = int(input())

li = []

for _ in range(n):
    s, e = map(int, input().split())
    li.append((s, e))

li = sorted(li, key=lambda a: a[0])
li = sorted(li, key=lambda a: a[1])

last = 0
cnt = 0

for start, end in li:
    if last <= start:
        last = end
        cnt += 1

print(cnt)

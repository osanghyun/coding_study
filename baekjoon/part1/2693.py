ret = []
for _ in range(int(input())):
    a = list(map(int, input().split()))
    a.sort()
    ret.append(a[-3])

for n in ret:
    print(n)

t = int(input())
rets = []
for i in range(t):
    first, second = map(int, input().split())
    rets.append(first+second)

for ret in rets:
    print(ret)
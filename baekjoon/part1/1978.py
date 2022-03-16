n = int(input())

data = list(map(int, input().split()))

ret = 0

for n in data:
    if n == 1:
        continue

    checker: bool = True

    for i in range(2, n):
        if n % i == 0:
            checker = False
            break

    if checker:
        ret += 1

print(ret)

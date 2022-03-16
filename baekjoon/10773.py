n = int(input())

ret = list()

for _ in range(n):
    num = int(input())

    if num == 0:
        ret.pop()
    else:
        ret.append(num)

print(sum(ret))

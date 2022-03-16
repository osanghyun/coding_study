t = int(input())

rets = []

for _ in range(t):
    n = int(input())
    binary_data = []
    ret = []

    while n > 0:
        binary_data.append(n % 2)
        n //= 2

    for i in range(len(binary_data)):
        if binary_data[i] == 1:
            ret.append(i)

    rets.append(ret)

for ret in rets:
    for n in ret:
        print(n, end=' ')
    print()

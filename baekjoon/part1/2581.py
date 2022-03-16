def is_prime(target: int) -> bool:
    if target == 1:
        return False

    for i in range(2, target):
        if target % i == 0:
            return False

    return True


m, n = int(input()), int(input())

ret = []

for num in range(m, n+1):
    if is_prime(num):
        ret.append(num)

if not ret:
    print(-1)
else:
    print(sum(ret))
    print(ret[0])

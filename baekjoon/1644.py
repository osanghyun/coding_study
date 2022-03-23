def eratones(target: int) -> list:
    check = [True] * (target + 1)

    for i in range(2, target + 1):
        if check[i]:
            for j in range(i + i, target + 1, i):
                check[j] = False

    ret = []
    for i in range(2, target + 1):
        if check[i]:
            ret.append(i)

    return ret


n = int(input())
primes = eratones(n)

left = 0
right = 0

ans: int = 0

while left <= right < len(primes):
    total: int = 0
    if right + 1 == len(primes):
        total = sum(primes[left:])
    else:
        total = sum(primes[left:right+1])

    if total == n:
        ans += 1
        right += 1
    elif total > n:
        left += 1
    else:
        right += 1

print(ans)

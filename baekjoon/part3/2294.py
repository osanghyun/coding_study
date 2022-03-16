n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

dp = [0] * (k+1)

for total in range(1, k+1):
    a = []

    for coin in coins:
        if coin <= total and dp[total - coin] != -1:
            a.append(dp[total - coin])

    if not a:
        dp[total] = -1
    else:
        dp[total] = min(a) + 1


print(dp[k])

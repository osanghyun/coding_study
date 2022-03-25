n = int(input())

time = []
price = []

for _ in range(n):
    t, p = map(int, input().split())
    time.append(t)
    price.append(p)

dp = [0] * (n + 1)

for i in range(n):
    if i + time[i] <= n:
        dp[i + time[i]] = max(dp[i + time[i]], dp[i] + price[i])
    dp[i+1] = max(dp[i+1], dp[i])

print(dp[n])

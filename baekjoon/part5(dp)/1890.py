import sys


input = sys.stdin.readline

n = int(input())

table = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:  # 목표 지점 도달.
            break

        if dp[i][j] == 0:
            continue

        distance = table[i][j]  # 점프 거리.

        if i + distance < n:  # 오른쪽 점프.
            dp[i+distance][j] += dp[i][j]
        if j + distance < n:  # 아랫쪽 점프.
            dp[i][j+distance] += dp[i][j]


print(dp[n-1][n-1])
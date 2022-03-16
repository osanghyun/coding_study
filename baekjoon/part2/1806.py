import sys

n, s = map(int, input().split())

sequence = list(map(int, input().split()))

left = 0
right = 0

ans: int = sys.maxsize

sum_value = 0

while True:
    if sum_value >= s:
        ans = min(ans, right - left)
        sum_value -= sequence[left]
        left += 1
    elif right == n:
        break
    else:
        sum_value += sequence[right]
        right += 1

if ans == sys.maxsize:
    print(0)
else:
    print(ans)

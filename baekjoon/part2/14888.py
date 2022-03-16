import sys

n = int(input())
nums = list(map(int, input().split()))
a, s, m, d = map(int, input().split())

max_ret, min_ret = -sys.maxsize-1, sys.maxsize


def solution(num, idx, add, sub, mul, div):
    global max_ret, min_ret
    if idx >= n:
        max_ret = max(max_ret, num)
        min_ret = min(min_ret, num)
        return

    if add > 0:
        solution(num + nums[idx], idx+1, add-1, sub, mul, div)
    if sub > 0:
        solution(num - nums[idx], idx+1, add, sub-1, mul, div)
    if mul > 0:
        solution(num * nums[idx], idx+1, add, sub, mul-1, div)
    if div > 0:
        solution(int(num / nums[idx]), idx+1, add, sub, mul, div-1)


solution(nums[0], 1, a, s, m, d)
print(max_ret)
print(min_ret)

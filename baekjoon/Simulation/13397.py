import itertools
import sys


def sum_interval(points: list) -> int:
    global arr
    ret: int = 0

    if len(points) == 1:
        ret = max(arr) - min(arr)
        return ret

    for idx, point in enumerate(points):
        if idx == 0:
            ret += max(arr[:point]) - min(arr[:point])
        elif idx == interval - 1:
            ret += max(arr[point-1:]) - min(arr[point-1:])
        else:
            ret += max(arr[points[idx-1]:point]) - min(arr[points[idx-1]:point])

    return ret


input = sys.stdin.readline

size, interval = map(int, input().split())

arr = list(map(int, input().split()))

ans: int = sys.maxsize

for divs in itertools.combinations([i for i in range(1, size)], interval):

    ans = min(ans, sum_interval(divs))

print(ans)

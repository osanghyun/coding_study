h, w = map(int, input().split())

heights = list(map(int, input().split()))

left = 0
right = len(heights)-1
left_max = 0
right_max = 0
ret: int = 0

while left <= right:
    left_max = max(left_max, heights[left])
    right_max = max(right_max, heights[right])

    if left_max <= right_max:
        ret += left_max - heights[left]
        left += 1
    else:
        ret += right_max - heights[right]
        right -= 1

print(ret)

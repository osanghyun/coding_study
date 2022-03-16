num = int(input())

heights = list(map(int, input().split()))

if num < 3:
    print(max(heights))
else:
    max_h = max(heights)

    for i in range(1, num-1):
        data = min(heights[i-1], heights[i+1])
        data += heights[i]
        max_h = max(max_h, data)

    print(max_h)


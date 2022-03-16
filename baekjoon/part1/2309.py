heights = [int(input()) for _ in range(9)]

total = sum(heights)

for index1 in range(9-1):
    for index2 in range(index1+1, 9):
        if 100 == total - heights[index1] - heights[index2]:
            h1, h2 = heights[index1], heights[index2]

            heights.remove(h1)
            heights.remove(h2)
            heights.sort()

            for height in heights:
                print(height)
            exit()

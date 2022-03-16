def binary_search(left: int, right: int, data: list[int], target: int) -> int:
    if left > right:
        return 0

    mid = (left + right) // 2

    if data[mid] == target:
        return 1
    elif data[mid] < target:
        return binary_search(mid+1, right, data, target)
    else:
        return binary_search(left, mid-1, data, target)


n = int(input())

nums = list(map(int, input().split()))

m = int(input())

targets = list(map(int, input().split()))

nums.sort()

for t in targets:
    print(binary_search(0, len(nums)-1, nums, t))

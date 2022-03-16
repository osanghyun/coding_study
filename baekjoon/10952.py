inputs = []
while True:
    first, second = map(int, input().split())

    if first == 0 and second == 0:
        break

    inputs.append((first, second))

for data in inputs:
    print(sum(data))
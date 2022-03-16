a, b = map(int, input().split())

sequence = []

num = 1
count = 1

while count <= b:
    for _ in range(num):
        sequence.append(num)
        count += 1
    num += 1

print(sum(sequence[a-1:b]))

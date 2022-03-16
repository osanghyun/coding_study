base = int(input())

cycle = 0

final = -1

first = base

while base != final:
    final = ((first % 10) * 10) + (((first // 10) + (first % 10)) % 10)

    first = final

    cycle += 1

print(cycle)

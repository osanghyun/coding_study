t = int(input())

cases = []

for _ in range(t):
    cases.append(list(map(int, input().split())))

for i in range(t):
    print(f'Case #{i+1}: {cases[i][0] + cases[i][1]}')
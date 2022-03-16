import collections

a = int(input())
b = int(input())
c = int(input())

num = str(a * b * c)

count = collections.defaultdict(int)

for i in num:
    count[i] += 1

for i in range(10):
    print(count[f'{i}'])
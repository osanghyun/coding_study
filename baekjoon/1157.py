import collections

strs = input()

if not strs:
    exit(0)

strs = strs.lower()

maps = collections.defaultdict(int)

for data in strs:
    maps[data] += 1

count = collections.Counter(maps).most_common(2)

if len(count) == 2 and count[0][1] == count[1][1]:
    print('?')
else:
    print(count[0][0].upper())
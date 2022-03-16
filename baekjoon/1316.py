import collections

n = int(input())

strs = list()

for _ in range(n):
    strs.append(input())

ret: int = 0

for s in strs:
    counter = collections.Counter(s)

    for i in range(len(s)-1):
        counter[s[i]] -= 1

        if s[i] != s[i+1] and counter[s[i]] != 0:
            ret -= 1
            break

    ret += 1

print(ret)

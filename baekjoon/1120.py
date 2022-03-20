import sys

a, b = input().split()

count: int = sys.maxsize

if len(a) == len(b):
    c: int = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            c += 1
    count = min(count, c)

elif len(a) < len(b):
    diff = len(b) - len(a)
    for i in range(diff+1):
        c: int = 0
        for j in range(i, i + len(a)):
            a_index = j - i
            if a[a_index] != b[j]:
                c += 1
        count = min(count, c)

elif len(a) > len(b):
    diff = len(a) - len(b)
    for i in range(diff+1):
        c: int = 0
        for j in range(i, i + len(b)):
            b_index = j - i
            if b[b_index] != a[j]:
                c += 1
        count = min(count, c)

print(count)
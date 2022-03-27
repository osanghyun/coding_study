import sys


input = sys.stdin.readline

s = input()

ans = [-1] * 26

for i, c in enumerate(s):
    if c.isalpha():
        idx = ord(c) - ord('a')
        if ans[idx] == -1:
            ans[idx] = i

for an in ans:
    print(an, end=' ')

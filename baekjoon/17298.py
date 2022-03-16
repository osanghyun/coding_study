"""
티어 : 골드4
시간 : 5분
분류 : 스택
"""

n = int(input())

sequence = list(map(int, input().split()))

stack = list()

output = [-1 for _ in range(n)]

for i in range(n):
    while stack and sequence[stack[-1]] < sequence[i]:
        output[stack[-1]] = sequence[i]
        stack.pop()
    stack.append(i)

for out in output:
    print(out, end=' ')
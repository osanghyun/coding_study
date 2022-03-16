n = int(input())

stack = list()

outputs = list()

for _ in range(n):
    order = list(input().split())

    if order[0] == 'push':
        stack.append(int(order[1]))
    elif order[0] == 'pop':
        if stack:
            outputs.append(stack.pop())
        else:
            outputs.append(-1)
    elif order[0] == 'size':
        outputs.append(len(stack))
    elif order[0] == 'empty':
        if stack:
            outputs.append(0)
        else:
            outputs.append(1)
    elif order[0] == 'top':
        if stack:
            outputs.append(stack[-1])
        else:
            outputs.append(-1)

for output in outputs:
    print(output)
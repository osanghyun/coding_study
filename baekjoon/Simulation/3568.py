import re


in_str: str = input()

in_str: str = re.sub(r'[,;]', '', in_str)

in_data: list = in_str.split()

default_type: str = in_data[0]
variables: list = in_data[1:]

for variable in variables:
    variable: str
    name = re.sub(r'[^a-zA-Z]', '', variable)
    add_type = re.sub(r'[a-zA-Z]', '', variable)
    stack = []
    for t in add_type:
        if t == '[':
            stack.append('[]')
        elif t == ']':
            continue
        else:
            stack.append(t)

    add_type = ''
    while stack:
        add_type += stack.pop()

    print(default_type + add_type + ' ' + name + ';')
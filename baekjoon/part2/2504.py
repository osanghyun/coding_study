stream = input()

match_table = {
    ')': '(',
    ']': '['
}
calc_table = {
    ')': 2,
    ']': 3
}


def is_right(s):  # 괄호열 판별.
    stack = []
    for char in s:
        if char not in match_table:  # '(' or '['
            stack.append(char)
        elif not stack or match_table[char] != stack.pop():  # ')' or ']'
            return False
    return len(stack) == 0


def calc_value(s):  # 올바른 괄호열에 대한 수 계산.
    stack = []

    for char in s:
        if char not in match_table:  # '(' or ']'
            stack.append(char)

        else:  # ')' or ']'
            temp: int = 0

            while stack[-1] != match_table[char]:  # 수 더하기.
                temp += stack.pop()

            if temp == 0:  # 내부 괄호 존재 x.
                stack[-1] = calc_table[char]
            else:  # 내부 괄호 존재 o.
                stack[-1] = calc_table[char] * temp

    print(sum(stack))


if is_right(stream):
    calc_value(stream)
else:
    print(0)

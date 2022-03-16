s, texts = input().split()

s = int(s)

width = s + 2
height = 2 * s + 3

numbers = [[' '] * (width * 10) for _ in range(height)]


def horizontal(col, s_num):
    global width
    for p in range(s_num+1, s_num+width-1):
        numbers[col][p] = '-'


def left_vertical(col, s_num):
    numbers[col][s_num] = '|'


def right_vertical(col, s_num):
    numbers[col][s_num + width - 1] = '|'


for idx, text in enumerate(texts):
    start = width * idx

    if text not in '14':
        horizontal(0, start)

    for num in range(s):
        if text not in '56':
            right_vertical(1+num, start)

        if text not in '1237':
            left_vertical(1+num, start)

    if text not in '170':
        horizontal(height//2, start)

    for num in range(s):
        if text not in '2':
            right_vertical(num+s+2, start)

        if text not in '134579':
            left_vertical(num+s+2, start)

    if text not in '147':
        horizontal(-1, start)

for i in range(height):
    for j in range(1, (width * 10)+1):
        if j % width == 0 and j != width * 10:
            print(numbers[i][j - 1], end=' ')
        elif j == width * 10:
            print(numbers[i][j - 1])
        else:
            print(numbers[i][j - 1], end='')


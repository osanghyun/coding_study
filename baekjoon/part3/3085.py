n = int(input())
table = [list(input()) for _ in range(n)]

ans: int = 0


def count(s_row, e_row, s_col, e_col):
    global table, n, ans
    for i in range(s_row, e_row + 1):
        row_num = 1
        for j in range(1, n):
            if table[i][j] == table[i][j-1]:
                row_num += 1
            else:
                row_num = 1

            ans = max(ans, row_num)

    for i in range(s_col, e_col + 1):
        col_num = 1
        for j in range(1, n):
            if table[j][i] == table[j-1][i]:
                col_num += 1
            else:
                col_num = 1
            ans = max(ans, col_num)


for x in range(n):
    for y in range(n):
        if y+1 < n:
            table[x][y], table[x][y+1] = table[x][y+1], table[x][y]
            count(x, x, y, y+1)
            table[x][y], table[x][y+1] = table[x][y+1], table[x][y]
        if x+1 < n:
            table[x][y], table[x+1][y] = table[x+1][y], table[x][y]
            count(x, x+1, y, y)
            table[x][y], table[x+1][y] = table[x+1][y], table[x][y]

print(ans)

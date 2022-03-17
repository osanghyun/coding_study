def get_dec(num, dec_nums, digit=1):
    if digit > 10:
        return

    dec_nums.append(num)

    for i in range(10):
        if num % 10 > i:
            get_dec((num * 10) + i, dec_nums, digit=digit + 1)

    return dec_nums


n = int(input())
dec_nums = []

for num in range(10):
    r = get_dec(num, dec_nums)

r.sort()

if n >= 1023:
    print(-1)
else:
    print(r[n])

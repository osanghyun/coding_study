from itertools import combinations


def convert(x):
    return ord(x) - ord('a')


def convert_2(arr):
    result = 0
    for a in arr:
        result |= (1 << a)
    return result


n, k = map(int, input().split())

default_chars = set(map(convert, ['a', 'c', 'i', 't', 'n']))

words = [set(map(convert, input().strip())) - default_chars for _ in range(n)]
bin_words = [convert_2(word) for word in words]

if k < 5:
    print(0)
else:
    bin_list = [i for i in range(ord('z')-ord('a')+1) if i not in default_chars]
    power_of_2 = [2 ** b for b in bin_list]
    max_count = 0
    for comb in combinations(power_of_2, k - 5):
        current = sum(comb)
        count = 0
        for bin_word in bin_words:
            if bin_word & current == bin_word:
                count += 1
        max_count = max(max_count, count)
    print(max_count)
    
n, k = map(int, input().split())

appliances = list(map(int, input().split()))

multi_taps = []

ans: int = 0

for i in range(k):
    if appliances[i] in multi_taps:
        continue
    elif len(multi_taps) < n:
        multi_taps.append(appliances[i])
        continue
    else:
        idxs = []
        for j in range(n):
            if multi_taps[j] in appliances[i:]:
                idx = appliances[i:].index(multi_taps[j])
            else:
                idx = 101
            idxs.append(idx)
        out_idx = idxs.index(max(idxs))
        del multi_taps[out_idx]
        multi_taps.append(appliances[i])
        ans += 1

print(ans)

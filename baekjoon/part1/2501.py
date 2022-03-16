n, k = map(int, input().split())

divisors = []

for num in range(1, n+1):
    if n % num == 0:
        divisors.append(num)

if len(divisors) < k:  # k번째 약수 존재 x.
    print(0)
else:
    print(divisors[k-1])  # k번째로 작은 약수 출력

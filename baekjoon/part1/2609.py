def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


num1, num2 = map(int, input().split())

num1, num2 = max(num1, num2), min(num1, num2)

print(gcd(num1, num2))
print(lcm(num1, num2))

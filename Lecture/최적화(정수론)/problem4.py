# 2436
g, l = map(int, input().split())

def _gcd(a, b):
    while a % b != 0:
        tmp = a % b
        a = b
        b = tmp
    return b

# 유클리드 호제법
def gcd(a, b):
    if a % b == 0:
        return b

    return gcd(b, a % b)

def _lcm(a, b):
    return a * b // _gcd(a, b)

import sys
input = sys.stdin.readline

def factorial(n):
    total = 1
    for i in range(n, 0, -1):
        total *= i
    return total

n, m = map(int, input().split())

print(factorial(n) // (factorial(n-m)*factorial(m)))

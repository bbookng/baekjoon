import sys

input = lambda: sys.stdin.readline().strip()

T = int(input())

for _ in range(T):
    N = int(input())
    phone_book = [input() for _ in range(N)]

    phone_book.sort()

    result = 'YES'

    for i in range(N - 1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            result = 'NO'
            break

    print(result)
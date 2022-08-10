n = [1, 2, 3, 4, 5, 6, 7, 8]

k = list(map(int, input().split()))


if n == k:
    print('ascending')
elif sorted(n, reverse=True) == k:
    print('descending')
else:
    print('mixed')


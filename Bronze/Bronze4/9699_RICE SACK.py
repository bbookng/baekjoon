T = int(input())
for i in range(T):
    arr = list(map(int, input().split()))
    print(f'Case #{i+1}: {max(arr)}')
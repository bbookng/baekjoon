a, b = map(int, input().split())

# for i in range(min(a, b), 0, -1):   # 최대공약수 구하기. a,b 중 작은수부터 -1하며 반복
#     if a % i == 0 and b % i == 0:   # i로 나누어 둘 다 나머지가 0일 때 최대 공약수
#         print(i)
#         break
#
# for j in range(max(a, b), (a*b)+1): # 최대공배수 구하기. a,b 중 큰 수부터 a*b까지 반복
#     if j % a == 0 and j % b == 0:   # j를 a, b로 나누었을 때 둘 다 나머지가 0일때 최소공배수
#         print(j)
#         break

# 위 코드는 시간초과로 '유클리스 호제법' 이용

n, m = max(a, b), min(a, b)

while m > 0:
    n, m = m, n % m

print(n)
print((a * b) // n)
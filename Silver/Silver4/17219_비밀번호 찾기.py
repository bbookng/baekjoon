import sys
input = lambda : sys.stdin.readline().strip()

N, M = map(int, input().split())
dict = {}
for i in range(N):
    address, pw = input().split()
    dict[address] = pw

for j in range(M):
    check = input()
    print(dict.get(check))

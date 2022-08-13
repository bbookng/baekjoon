import sys
input = sys.stdin.readline

C, R = map(int, input().split())
K = int(input())

if K > C*R:
    print(0)

while True:
    


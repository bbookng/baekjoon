import sys
input = sys.stdin.readline

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

p = (p+t) % (w*2)
q = (q+t) % (h*2)

if p > w:
    p = w*2 - p
if q > h:
    q = h*2 - q

print(p, q)

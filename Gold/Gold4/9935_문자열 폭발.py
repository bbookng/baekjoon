import sys
input = lambda :sys.stdin.readline().strip()

text = input()
target = list(input())

stack = []

for i in text:
    stack.append(i)
    if i == target[-1]:
        if stack[-len(target):] == target:
            for j in range(len(target)):
                stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')




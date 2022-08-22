import sys
input = lambda : sys.stdin.readline().strip()

N = input()
stack = []

for i in N:
    if i == '(':
        stack.append(i)
    elif i == ')':
        while stack and stack[-1] != '(':
            print(stack.pop(), end='')
        if stack[-1] == '(':
            stack.pop()
    elif i in '+-':
        while stack and stack[-1] != '(':
            print(stack.pop(), end='')
        stack.append(i)
    elif i in '*/':
        while stack and stack[-1] in '*/':
            print(stack.pop(), end='')
        stack.append(i)
    else:
        print(i, end='')

while stack:
    print(stack.pop(), end='')

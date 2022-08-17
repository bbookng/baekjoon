# import sys
# input = lambda:sys.stdin.readline().strip()
#
# N = input()
#
# i = 0
# numbers = []
# operators = []
# tmp = ''
# while i < len(N):
#     if N[i].isdecimal():
#         tmp += N[i]
#     else:
#         numbers.append(int(tmp))
#         tmp = ''
#         operators.append(N[i])
#     i += 1
# numbers.append(int(tmp))
#
# i = 0
# while i < len(operators):
#     if operators[i] != "+":
#         i += 1
#     else:
#         numbers[i] = numbers[i]+numbers[i+1]
#         numbers.pop(i+1)
#         operators.pop(i)
#
# total = numbers[0]
# for i in range(1, len(numbers)):
#     total -= numbers[i]
# print(total)

string = input().split('-')
arr = []

for plus_deonguhri in string:
    tmp = 0
    for number in plus_deonguhri.split('+'):
        tmp += int(number)
    arr.append(tmp)

total = arr[0]
for i in range(1, len(arr)):
    total -= arr[i]

print(total)
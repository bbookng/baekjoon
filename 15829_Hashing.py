l = int(input())
word = input()

result = 0
for i in range(l):
    num = ord(word[i])-96
    result += num * (31 ** i)

print(result % 1234567891)

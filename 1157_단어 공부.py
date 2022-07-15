word = input()

d = dict()
for chr in word:
    chr = chr.upper()
    if chr in d:
        d[chr] += 1
    else:
        d[chr] = 1

flag = 0
result = max(d.values())
answer = '?'
for k, v in d.items():

    if v == result:
        flag += 1
        if flag == 2:
            answer = '?'
        else:
            answer = k

print(answer)

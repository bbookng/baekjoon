import requests
from random import sample

URI = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1"
lucky = requests.get(URI).json()
answer = set()
for i in range(1, 7):
    answer.add(lucky[f'drwtNo{i}'])
bonus = lucky['bnusNo']

result = [0] * 7
for i in range(1000):
    tmp = set(sample(list(range(1, 46)), 6))
    n = answer & tmp
    if len(n) == 6:
        result[1] += 1
    elif len(n) == 5 and bonus in tmp:
        result[2] += 1
    elif len(n) == 5:
        result[3] += 1
    elif len(n) == 4:
        result[4] += 1
    elif len(n) == 3:
        result[5] += 1
    else:
        result[6] += 1

print(result)
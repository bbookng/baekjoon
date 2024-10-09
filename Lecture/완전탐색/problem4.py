# 문제 4. 숫자야구 (# 2503)

n = int(input())

hint = [list(map(int, input().split())) for _ in range(n)]

answer = 0

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            if a == b or b == c or c == a:
                continue

            cnt = 0
            for arr in hint:
                number = str(arr[0])
                strike = arr[1]
                ball = arr[2]

                ball_count = 0
                strike_count = 0

                # 비교할 수 (a, b, c)를 문자열로 만듦
                guess = str(a) + str(b) + str(c)

                # 스트라이크와 볼 개수 세기
                for i in range(3):
                    if guess[i] == number[i]:
                        strike_count += 1  # 자리가 같으면 스트라이크
                    elif guess[i] in number:
                        ball_count += 1  # 자리는 다르지만 숫자가 포함되면 볼

                if ball == ball_count and strike == strike_count:
                    cnt += 1

            if cnt == n:
                answer += 1

print(answer)
T = int(input())

for _ in range(T):
    now = 0
    frame = 1
    count = 0
    total = 0
    scores = list(map(int, input().split()))
    i = 0
    while frame <= 10 and i < len(scores):
        if scores[i] == 10:
            # 스트라이크 처리
            total += 10 + scores[i+1] + scores[i+2]
            frame += 1
            i += 1
        else:
            # 첫 번째 투구
            now = scores[i]
            i += 1
            if i < len(scores):
                # 두 번째 투구
                now += scores[i]
                if now == 10:
                    # 스페어 처리
                    total += 10 + scores[i+1]
                else:
                    total += now
                i += 1
            frame += 1
    print(total)

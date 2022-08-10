t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())
    result = [i for i in range(1, n+1)]        # 0층의 각 호에 사는 사람의 수 list 생성
    for _ in range(k):                         # 층만큼 반복
        for j in range(1, n):                  # 1호실 부터 n호실 까지 반복
            result[j] += result[j-1]           # 1호부터 n호까지 값 누적
    print(result[-1])                          # 최종 k층 n호실 거주인 수 출력
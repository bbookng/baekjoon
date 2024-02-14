def findMaxDistinctItems(n, arr, k):
    # 이미 구매한 아이템을 집합으로 변환
    purchased_items = set(arr)

    # 아이템의 가격을 1부터 n까지 반복하면서 확인
    for i in range(1, n + 1):
        # 이미 구매한 아이템인 경우 무시
        if i in purchased_items:
            continue

        # 남은 돈으로 현재 아이템을 구매할 수 있는지 확인
        if i <= k:
            # 구매 가능하면 아이템을 추가하고 가격을 차감
            purchased_items.add(i)
            k -= i
        else:
            # 더 이상 아이템을 구매할 수 없으면 종료
            break

    # 집합에 있는 고유 아이템 수를 반환
    return len(purchased_items)


# 예제 입력에 대한 실행
n = 10
arr = [1, 3, 8]
k = 10
result = findMaxDistinctItems(n, arr, k)
print(result)  # 출력: 5

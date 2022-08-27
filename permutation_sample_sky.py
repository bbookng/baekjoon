# 한 행에서 column을 선택하고 다음 행으로 갈 때마다 이 함수가 불리운다.
# chosen는 앞 선 행에서 선택된 column을 기록하고 있다.

def perm(row, chosen) :
    if row == N :                   # 마지막 열까지 왔으니
        print('row == N(3)', chosen)
        return

    for i in range(N) :
        if i in chosen :
            continue
        chosen[row] = i
        perm(row+1, chosen)
        chosen[row] = -1



N = 3
data = [['A', 'B', 'C'],
        ['D', 'E', 'F'],
        ['G', 'H', 'I']]
chosen = [-1 for _ in range(N)]     # 각 행에서 선택한 열을 기록하기 위함

perm(0, chosen)

N = int(input())

nodes = list(map(int, input().split()))
X = int(input())

nodes[nodes.index(-1)] = X
nodes.sort()


def solution(n, d):
    if not d:
        print(nodes[n], d)
        return
    if nodes[n - d]:
        solution(n - d, d//2)
    if nodes[n + d]:
        solution(n + d, d//2)
    print(nodes[n], d)

solution(N // 2, (N+1)//4)
from collections import defaultdict, deque

def getPoint(d, ee):
    candidate = []
    for k in d.keys():
        if len(d[k]) > 1:
            candidate.append(k)

    for node in candidate:
        if node not in set(ee):
            return node

def judge(d, start):
    visited = [start]
    q = deque([start])

    while q:
        now = q.popleft()
        if len(d[now]) > 1:
            return 3

        for nxt in d[now]:
            if nxt not in visited:
                q.append(nxt)
            else:
                return 1
    return 2

def solution(edges):

    d = defaultdict(list)
    ee = []
    for s, e in edges:
        d[s].append(e)
        ee.append(e)

    point = getPoint(d, ee)

    result = [point, 0, 0, 0]

    for start in d[point]:
        result[judge(d, start)] += 1

    return result
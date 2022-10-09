import sys
input = sys.stdin.readline

V = int(input())
E = int(input())
rep = [i for i in range(V+1)]
join = {i: [i] for i in range(V+1)}

info = []
for i in range(E):
    info.append(list(map(int, input().split())))

info.sort(key=lambda x: x[2])
selected = 0
i = 0
total = 0
while i < E:
    u, v, w = info[i][0], info[i][1], info[i][2]

    if rep[u] == rep[v]:
        i += 1
        continue

    total += w
    selected += 1
    i += 1

    if rep[u] < rep[v]:
        for vv in join[rep[v]]:
            join[rep[u]].append(vv)
            rep[vv] = rep[u]
    else:
        for uu in join[rep[u]]:
            join[rep[v]].append(uu)
            rep[uu] = rep[v]

print(total)

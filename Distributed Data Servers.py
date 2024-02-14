import sys
sys.setrecursionlimit(10 ** 5)

def getMaxTime(g_nodes, g_from, g_to):
    graph = [[] for _ in range(g_nodes + 1)]

    def dfs(node, visited):
        visited[node] = True
        max_distance = 0
        max_distance_node = node

        for next_node in graph[node]:
            if not visited[next_node]:
                distance, next_node = dfs(next_node, visited)
                if distance + 1 > max_distance:
                    max_distance = distance + 1
                    max_distance_node = next_node

        return max_distance, max_distance_node

    for i in range(len(g_from)):
        f, t = g_from[i], g_to[i]
        graph[f].append(t)
        graph[t].append(f)

    max_time, node = dfs(1, [False] * (g_nodes + 1))
    max_time, node = dfs(node, [False] * (g_nodes + 1))

    return max_time


print(getMaxTime(3, [1, 2], [2, 3]))
# print(getMaxTime(5, [1, 5, 1, 5], [5, 3, 2, 4]))
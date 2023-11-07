def dfs(idx1, idx2, number):
    if len(number) == 6:
        result.add(number)
        return
    move = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    for (x, y) in move:
        nextIdx1 = idx1 + x
        nextIdx2 = idx2 + y
        if 0 <= nextIdx1 < 5 and 0 <= nextIdx2 < 5:
            dfs(nextIdx1, nextIdx2, number + graph[nextIdx1][nextIdx2])

graph = []
result = set()

for i in range(5):
    graph.append(input().split())

for x in range(5):
    for y in range(5):
        dfs(x, y, graph[x][y])

print(len(result))

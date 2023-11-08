import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

count = 1

def dfs(start):
    global count
    visited[start] = count

    for i in graph[start]:
        if visited[i] == 0:
            count += 1
            dfs(i)

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for track in graph:
    track.sort()

dfs(v)

for i in visited[1:]:
    print(i)

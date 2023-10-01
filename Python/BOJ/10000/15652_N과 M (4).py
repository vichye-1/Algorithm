# dfs() 함수 사용
n, m = list(map(int, input().split()))

result = []

def dfs(start):
    if len(result) == m:
        print(" ".join(map(str, result)))
        return

    for i in range(start, n + 1):
        result.append(i)
        dfs(i)
        result.pop()

dfs(1)

# combinations_with_replacement 사용
from itertools import combinations_with_replacement
n, m = map(int, input().split())
for a in combinations_with_replacement(map(str, range(1, n + 1)), m):
    print(" ".join(a))

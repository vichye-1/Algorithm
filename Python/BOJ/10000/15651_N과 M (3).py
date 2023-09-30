# dfs 함수 사용
n, m = list(map(int, input().split()))
numList = [_ for _ in range(1, n + 1)]
result = []

def dfs(start):
    if len(result) == m:
        print(" ".join(map(str, result)))
        return

    for i in numList:
        result.append(i)
        dfs(i)
        result.pop()

dfs(1)

# product 사용
from itertools import product

n, m = map(int, input().split())

numList = [str(_) for _ in range(1, n + 1)]

print("\n".join(list(map(" ".join, product(numList, repeat = m)))))

# dfs() 함수 이용
n, m = map(int, input().split())
numList = list(map(int, input().split()))
numList.sort()
result = []
def dfs(start):
    if len(result) == m:
        print(" ".join(map(str, result)))
        return
    
    for i in range(start, n):
        if numList[i] not in result:
            result.append(numList[i])
            dfs(i + 1)
            result.pop()

dfs(0)

# combinations 사용
from itertools import combinations
n, m = map(int, input().split())
numList = list(map(int, input().split()))
numList.sort()
result = list(combinations(numList, m))
for i in result:
    print(" ".join(map(str, i)))

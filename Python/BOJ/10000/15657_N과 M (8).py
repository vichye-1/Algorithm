# dfs() 사용
n, m = map(int, input().split())
numList = list(map(int, input().split()))
numList.sort()
result = []

def dfs(start):
    if len(result) == m:
        print(" ".join(map(str, result)))
        return
    
    for i in range(start, n):
        result.append(numList[i])
        dfs(i)
        result.pop()
dfs(0)

# combinations_with_replacement 사용
from itertools import combinations_with_replacement
n, m = map(int, input().split())
numList = list(map(int, input().split()))
numList.sort()
result = list(combinations_with_replacement(numList, m))
for i in result:
    print(" ".join(map(str, i)))

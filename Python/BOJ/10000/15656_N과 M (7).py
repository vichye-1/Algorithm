# dfs() 함수 사용
n, m = map(int, input().split())
numList = list(map(int, input().split()))
numList.sort()
result = []

def dfs(start):
    if len(result) == m:
        print(" ".join(map(str, result)))
        return
    
    for i in range(n):
        result.append(numList[i])
        dfs(i)
        result.pop()

dfs(0)

# product 사용
from itertools import product
n, m = map(int, input().split())
numList = list(map(int, input().split()))
numList.sort()
result = list(product(numList, repeat = m))
for i in result:
    print(" ".join(map(str, i)))

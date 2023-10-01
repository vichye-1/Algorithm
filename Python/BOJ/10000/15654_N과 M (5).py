# dfs() 함수 이용
n, m = map(int, input().split())
numList = sorted(list(map(int, input().split())))
result = []

def dfs():
    if len(result) == m:
        print(" ".join(map(str, result)))
        return
    
    for i in numList:
        if i not in result:
            result.append(i)
            dfs()
            result.pop()

dfs()

#permutations 사용
from itertools import permutations
n, m = map(int, input().split())
numList = sorted(list(map(int, input().split())))
for i in permutations(numList, m):
    print(" ".join(map(str, i)))

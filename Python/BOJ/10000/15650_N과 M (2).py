# dfs 함수 이용
n, m = list(map(int, input().split()))

array = []

def dfs(start):
    if len(array) == m:
        print(" ".join(map(str, array)))
    
    for i in range(start, n + 1):
        if i not in array:
            array.append(i)
            dfs(i + 1)
            array.pop()
            
dfs(1)

# itertools 사용 - 1
from itertools import combinations 
n, m = list(map(int, input().split()))
numList = [str(i) for i in range(1, n + 1)]
result = list(combinations(numList, m))
for i in result:
    print(" ".join(i))

# itertools 사용 - 2
from itertools import combinations 
n, m = list(map(int, input().split()))
numList = [i for i in range(1, n + 1)]
for i in combinations(numList, m):
    print(*i)

# dfs 함수 이용
n, m = list(map(int, input().split()))

array = []

def dfs():
    if len(array) == m:
        print(" ".join(map(str, array)))
    
    for i in range(1, n + 1):
        if i not in array:
            array.append(i)
            dfs()
            array.pop()

dfs()

# itertools 사용 - 더 빠름
import itertools

n, m = list(map(int, input().split()))
array = [str(i) for i in range(1, n + 1)]
results = itertools.permutations(array, m)

print('\n'.join(" ".join(result) for result in results))

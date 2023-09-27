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

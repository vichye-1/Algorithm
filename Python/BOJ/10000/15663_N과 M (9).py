n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [False] * n
result = []

def dfs():
    if len(result) == m:
        print(" ".join(map(str, result)))
        return
    overlap = 0
    for i in range(n):
        if not visited[i] and overlap != nums[i]:
            visited[i] = True
            result.append(nums[i])
            overlap = nums[i]
            dfs()
            visited[i] = False
            result.pop()
dfs()

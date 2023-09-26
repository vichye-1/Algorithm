n = int(input())
dp = [0 for _ in range(n + 1)]
plan = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(i + plan[i][0], n + 1):
        if dp[j] < dp[i] + plan[i][1]:
            dp[j] = dp[i] + plan[i][1]

print(dp[-1])

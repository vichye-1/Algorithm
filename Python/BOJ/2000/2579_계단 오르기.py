n = int(input())

stairs = [0] * n
for i in range(n):
    stairs[i] = int(input())

dp = [0] * n
for i in range(n):
    if i == 0:
        dp[0] = stairs[0]
    elif i == 1:
        dp[1] = stairs[1] + stairs[0]
    elif i == 2:
        dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])
    elif i > 2:
        dp[i] = max(dp[i - 2] + stairs[i], stairs[i] + stairs[i - 1] + dp[i - 3])
print(dp[n - 1])

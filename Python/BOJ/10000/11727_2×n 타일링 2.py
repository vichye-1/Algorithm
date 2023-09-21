n = int(input())
dp = [0] * (n + 1)
for i in range(n + 1):
    if i == 1:
        dp[1] = 1
    elif i == 2:
        dp[2] = 3
    else:
        dp[i] = dp[i - 1] + 2 * dp[i - 2]
print(dp[i] % 10007)

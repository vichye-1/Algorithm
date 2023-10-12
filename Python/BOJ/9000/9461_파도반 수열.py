# 방법 1
dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
for i in range(4, 101):
    dp[i] = dp[i - 2] + dp[i - 3]

for _ in range(int(input())):
    print(dp[int(input())])

# 방법 2
dp = [1, 1, 1, 2, 2]

for i in range(95):
    dp.append(dp[-1] + dp[-5])

for _ in range(int(input())):
    print(dp[int(input()) - 1])

# 제출한 풀이 - 40ms
x = int(input())
dp = [0] * (x + 1)

for i in range(1, x + 1):
    if i == 1:
        dp[1] = 1
    elif i == 2:
        dp[2] = 2
    else:
        dp[i] = dp[i - 2] + dp[i - 1]

print(dp[x] % 10007)

# 더 간단한 풀이 - 40ms
a = b = 1
for _ in range(int(input())):
    a, b = b, a + b
print(a % 10007)

# 다른 풀이 - 80ms
x = int(input())
dp = [0, 1, 2]
for i in range(3, x + 1):
    dp.append(dp[i - 2] + dp[i - 1])

print(dp[x] % 10007)

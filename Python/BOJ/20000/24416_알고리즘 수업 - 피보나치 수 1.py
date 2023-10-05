# 문제의 수도 코드를 이용하여 푼 버전
n = int(input())

def rec(n):
    fib = [0] * (n + 1)
    fib[1] = 1
    fib[2] = 1
    for i in range(3, n + 1):
        fib[i] = fib[i - 2] + fib[i - 1]
    return fib[n]

def dp(n):
    fib = [0] * (n + 1)
    fib[1] = 1
    fib[2] = 1
    count = 0
    for i in range(3, n + 1):
        count += 1
        fib[i] = fib[i - 2] + fib[i - 1]
    return count

print(rec(n), dp(n))

# 짧은 버전
n = int(input())
dp = [0, 1, 1]
for i in range(3, n + 1):
    dp.append(dp[i - 2] + dp[i - 1])
print(dp[n], n - 2)

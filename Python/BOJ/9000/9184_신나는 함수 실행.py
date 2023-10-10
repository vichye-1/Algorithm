def rec(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return rec(20, 20, 20)
    if dp[a][b][c]:
        return dp[a][b][c]
    if a < b < c:
        dp[a][b][c] = rec(a, b, c - 1) + rec(a, b - 1, c - 1) - rec(a, b - 1, c)
    else:
        dp[a][b][c] = rec(a - 1, b, c) + rec(a - 1, b - 1, c) + rec(a - 1, b, c - 1) - rec(a - 1, b - 1, c - 1)
    return dp[a][b][c]
    
dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]

while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break
    print(f"w({a}, {b}, {c}) = {rec(a, b, c)}")

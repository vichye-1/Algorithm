# 백트래킹
n = int(input())
nums = list(map(int, input().split()))
operator = list(map(int, input().split()))

# 1e9 = 1 * (10^9)
maxNum = -1e9
minNum = 1e9

# divide에서 total// nums[depth]를 하면 문제를 만족시키지 않는다.
def dfs(depth, total, plus, minus, multiply, divide):
    global maxNum, minNum
    if depth == n:
        maxNum = max(total, maxNum)
        minNum = min(total, minNum)
        return
    if plus:
        dfs(depth + 1, total + nums[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - nums[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * nums[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / nums[depth]), plus, minus, multiply, divide - 1)

dfs(1, nums[0], operator[0], operator[1], operator[2], operator[3])
print(maxNum)
print(minNum)

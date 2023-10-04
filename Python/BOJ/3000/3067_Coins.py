for _ in range(int(input())):
    n = int(input())
    coins = list(map(int, input().split()))
    money = int(input())
    dp = [0] * (money + 1)

    for coin in coins:
        if coin > money:
            continue
        dp[coin] += 1
        for i in range(coin + 1, money + 1):
            dp[i] += dp[i - coin]
    print(dp[money])

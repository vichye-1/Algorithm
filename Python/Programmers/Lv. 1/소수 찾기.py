def solution(n):
    check = [0] * 2 + [1] * (n - 1)
    for i in range(2, n + 1):
        if check[i]:
            for j in range(i * i, n + 1, i):
                check[j] = 0
    return sum(check)

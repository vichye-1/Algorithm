def binary(num):
    result = ""
    while num:
        mod = num % 2
        num = num // 2
        result += str(mod)
    return result
        
for _ in range(int(input())):
    n = int(input())
    target = binary(n)
    answer = []
    for i in range(len(target)):
        if target[i] == "1":
            answer.append(i)
    print(*answer)

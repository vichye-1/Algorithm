answer = []
for _ in range(int(input())):
    num = int(input())
    if num == 0:
        answer.pop()
    else:
        answer.append(num)
print(sum(answer))

n = int(input())
row = list(map(int, input().split()))

row.sort()

results = []
answer = 0
for num in row:
    answer += num
    results.append(answer)
print(sum(results))

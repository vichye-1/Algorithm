table = [0] * 10001
table[1] = 1

n = int(input())
for i in range(2, len(table)):
    table[i] = table[i - 2] + table[i - 1]

print(table[n])

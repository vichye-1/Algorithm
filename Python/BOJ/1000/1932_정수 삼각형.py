n = int(input())
pyramid = []
for _ in range(n):
    pyramid.append(list(map(int, input().split())))

for i in range(n - 2, -1, -1): # 3 2 1 0
    for j in range(i + 1):
        pyramid[i][j] += max(pyramid[i + 1][j], pyramid[i + 1][j + 1])
        
print(pyramid[0][0])

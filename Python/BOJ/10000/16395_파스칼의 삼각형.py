import math

row, th = map(int, input().split())
print(math.comb(row - 1, th - 1))

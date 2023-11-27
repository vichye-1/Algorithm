import math

row, th = map(int, input().split())
print(math.comb(row - 1, th - 1))

# math.comb(n, r) , math.perm(n, r) 을 처음 안 날. 
# 단순히 개수만 구하고 싶으면 itertools > len(list(combinations()))를 쓰지 않아도 됨.
# 오히려 'itertools > len(list(combinations()))'를 쓰면 메모리 초과가 남

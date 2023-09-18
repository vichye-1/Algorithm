n, m = map(int, input().split(" "))
answer = 0
str_dict = {}

for _ in range(n):
  str_dict[input()] = True

for _ in range(m):
  if input() in str_dict:
    answer += 1

print(answer)

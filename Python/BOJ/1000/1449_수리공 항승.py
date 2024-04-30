n, length = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
target = array[0]
answer = 1

for num in array[1:]:
    if target + length - 1 >= num:
        continue
    answer += 1
    target = num

print(answer)

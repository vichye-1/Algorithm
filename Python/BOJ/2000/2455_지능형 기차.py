maxNum = 0
curr = 0
for _ in range(4):
    peopleOut, peopleIn = map(int, input().split())
    curr += (peopleIn - peopleOut)
    maxNum = max(maxNum, curr)
print(maxNum)

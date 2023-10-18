# 답을 담을 변수 answer
answer = 0

# 이름을 담을 set
hi = set()

for _ in range(int(input())):
    enter = input()
    # 이름이 들어오면 set에 이름을 넣음
    if enter != "ENTER":
        hi.add(enter)
    # ENTER 가 들어오면 set의 길이를 answer에 더하고, set을 초기화
    else:
        answer += len(hi)
        hi.clear()
        
# 이름을 담는 set에 원소가 남아있으면 그 길이를 answer에 담음
if hi:
    answer += len(hi)
print(answer)

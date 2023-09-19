import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 빈 딕셔너리
dict = {}

# 딕셔너리에 '숫자 : 이름 / 이름: 숫자'로 저장
for i in range(1, n + 1):
  name = input().rstrip()
  dict[i] = name
  dict[name] = i

# 숫자면 int로 형 변환하여 value 출력, 숫자가 아니면 string 그대로 key값에 넣고 value 출력
for _ in range(m):
  question = input().rstrip()
  if question.isnumeric():
    print(dict[int(question)])
  else:
    print(dict[question])

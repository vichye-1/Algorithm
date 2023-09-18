import sys
input = sys.stdin.readline

count = int(input())
check = {}
inList = []

# 'enter'이면 딕셔너리에 {이름:1}, 'leave'이면 딕셔너리에 {이름:0}
for _ in range(count):
  info = input().split()
  if info[1] == "enter":
    check[info[0]] = 1
  else:
    check[info[0]] = 0

# value의 값이 1이면 리스트에 추가
for name in check:
  if check[name] == 1:
    inList.append(name)

# 내림차순으로 정렬
inList.sort(reverse = True)

# 리스트에서 join써서 원소 출력
print("\n".join(inList))

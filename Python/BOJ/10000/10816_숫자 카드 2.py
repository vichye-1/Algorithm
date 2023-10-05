n = int(input())
own = list(map(int, input().split()))
m = int(input())
cards = list(map(int, input().split()))

# 빈 딕셔너리 생성
# 카드의 종류 : 카드의 개수
# 예 - {6: 1, 3: 2, 2: 1, 10: 3, -10: 2, 7: 1}
card_dict = {}

# 상근이가 가지고 있는 카드를 돌면서 
# 만약 빈 딕셔너리에 키 값이 없으면 {카드 : 1}, 키 값이 존재하면 value에 1을 추가
for i in own:
    if i not in card_dict:
        card_dict[i] = 1
    else:
        card_dict[i] += 1

# 0이 m개인 리스트 생성
result = [0] * m

# 검증해야할 카드를 인덱스 순서대로 하나씩 돌면서
# 만약 검증해야 할 카드가 딕셔너리에 존재한다면, 검증해야할 카드에 해당하는 인덱스에 value의 값을 저장
for i in range(len(cards)):
    if cards[i] in card_dict:
        result[i] = card_dict[cards[i]]

# result 리스트 언패킹
print(*result)

word = input()

# -1로 된 리스트를 26개(알파벳 개수만큼) 만듦
result = [-1] * 26

# input값인 word를 for loop로 한 character씩 돌면서, find()로 인덱스 번호 추출
# (character의 아스키 코드 - 'a'의 아스키코드)를 하면 해당 알파벳의 인덱스를 구할 수 있음 (예 : 알파벳 'b'의 아스키코드(98) - 알파벳 'a'의 아스키코드(97) = 1. 알파벳 'b'의 인덱스는 1)
# 'result'리스트의 인덱스에 find()로 구한 input 단어 속 알파벳 인덱스를 'result'리스트에 넣음
for c in word:
    place = word.find(c)
    result[ord(c) - ord('a')] = place

# 'result'리스트 언패킹 
print(*result)

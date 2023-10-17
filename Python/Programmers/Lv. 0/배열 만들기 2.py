def solution(l, r):
    answer = []
    numList = [i for i in range(l, r + 1)]
    numList = list(map(str, numList))
    for i in numList:
        if set(i) == {'5'} or set(i) == {'5', '0'}:
            answer.append(int(i))
    if len(answer) == 0:
        return [-1]
    return answer

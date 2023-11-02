def solution(k, score):
    answer = []
    maxNums = []
    for num in score:
        maxNums.append(num)
        if len(maxNums) > k:
            maxNums.remove(min(maxNums))
        answer.append(min(maxNums))
    return answer

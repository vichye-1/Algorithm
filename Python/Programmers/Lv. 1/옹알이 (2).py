def solution(babbling):
    answer = 0
    canSay = ["aya", "ye", "woo", "ma"]
    for word in babbling:
        for can in canSay:
            if can * 2 not in word:
                word = word.replace(can, "0")
        if word.isnumeric():
            answer += 1
    return answer

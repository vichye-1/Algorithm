def solution(babbling):
    only = ["aya", "ye", "woo", "ma"]
    answer = 0
    for i in range(len(babbling)):
        for j in only:
            if j in babbling[i]:
                babbling[i] = babbling[i].replace(j, "0")

    for i in babbling:
        if i.isnumeric():
            answer += 1

    return answer

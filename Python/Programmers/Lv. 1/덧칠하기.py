def solution(n, m, section):
    answer, paint = 0, 0
    for num in section:
        if paint <= num:
            paint = num + m
            answer += 1
    return answer

def solution(s):
    answer = []
    s = s.lstrip("{").rstrip("}").split("},{")
    s.sort(key = len)
    for strnum in s:
        strnum = list(map(int, strnum.split(",")))
        for value in strnum:
            if value not in answer:
                answer.append(value)
    return answer

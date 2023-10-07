def solution(babbling):
    
    # 말 할 수 있는 단어 나열
    only = ["aya", "ye", "woo", "ma"]
    answer = 0

    # 'babbling'과 'only'를 돌면서 'only'에 있는 단어가 나오면 문자열"0"으로 바꿈(replace는 문자열만 취급하기 때문)
    for i in range(len(babbling)):
        for j in only:
            if j in babbling[i]:
                babbling[i] = babbling[i].replace(j, "0")
                
    # replace로 바뀐 'babbling'을 돌면서 'isnumeric()'실행. 
    # 만약 모두 말 할 수 있는 단어일경우 'babbling'속 단어는 무조건 숫자로 이루어져있을 것임
    # 'babbling'을 돌며 모두 숫자인 경우 'answer'에 +1 을 해준다
    for i in babbling:
        if i.isnumeric():
            answer += 1
            
    # 답 출력
    return answer

def solution(n, arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        answer.append(bin(arr1[i] | arr2[i])[2:])
        answer[i] = (" " * (n - len(answer[i]))) + answer[i].replace("1", "#").replace("0", " ")
    return answer

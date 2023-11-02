def solution(arr):
    answer = [arr[0]]
    target = arr[0]
    for i in range(1, len(arr)):
        if arr[i] != target:
            answer.append(arr[i])
            target = arr[i]
    return answer

def solution(arr):
    answer = []
    min = arr[0]
    for i in arr:
        if i < min:
            min = i
    for i in arr:
        if i is not min:
            answer.append(i)
    if not answer:
        answer.append(-1)
    return answer

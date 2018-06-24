def solution(arr):
    answer = []
    temp = arr[0]
    for i in arr:
        if temp != i:
            answer.append(temp)
            temp = i
    answer.append(arr[len(arr)-1])
    return answer

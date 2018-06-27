def solution(arr1, arr2):
    base = []
    answer = []
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            temp = int(arr1[i][j]) + int(arr2[i][j])
            base.append(temp)
        answer.append(base)
        base = []
    return answer

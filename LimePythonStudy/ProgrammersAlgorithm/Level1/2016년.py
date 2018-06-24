def solution(a, b):
    monthForDays = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    allDays = 0
    for i in range(a-1):
        allDays += monthForDays[i]
    allDays += b - 1
    result = allDays % 7
    if result == 0:
        answer = "FRI"
    elif result == 1:
        answer = "SAT"
    elif result == 2:
        answer = "SUN"
    elif result == 3:
        answer = "MON"
    elif result == 4:
        answer = "TUE"
    elif result == 5:
        answer = "WED"
    else:
        answer = "THU"
    return answer

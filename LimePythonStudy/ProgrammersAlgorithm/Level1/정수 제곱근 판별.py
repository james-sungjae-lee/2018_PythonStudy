import math

def solution(n):
    answer = math.sqrt(n)
    if answer != round(answer):
        answer = -1
    else:
        answer = (answer + 1)**2
    return answer

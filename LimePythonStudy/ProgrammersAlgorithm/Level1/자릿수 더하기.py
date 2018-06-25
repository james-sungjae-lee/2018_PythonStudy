def solution(n):
    data = list(str(n))
    data = list(map(int, data))
    answer = 0
    for i in data:
        answer += i
    return answer

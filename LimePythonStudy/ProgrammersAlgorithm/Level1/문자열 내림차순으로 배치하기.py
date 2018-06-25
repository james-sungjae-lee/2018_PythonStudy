def solution(s):
    data = list(s)
    data.sort(reverse = True)
    answer = ''
    for i in data:
        answer += i
    return answer

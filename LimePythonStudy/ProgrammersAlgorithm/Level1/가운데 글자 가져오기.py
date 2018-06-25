def solution(s):
    answer = ''
    strlen = len(s)
    index = int(strlen/2)

    if strlen is 1 or strlen is 2:
        return s

    if strlen % 2 == 1:
        answer += s[index]
    else:
        answer += s[index - 1]
        answer += s[index]
    return answer

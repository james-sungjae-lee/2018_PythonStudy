def solution(s):
    answer = ''
    checkUpper = True
    for i in range(len(s)):
        if s[i] == ' ':
            answer += s[i]
            checkUpper = True
        else:
            if checkUpper == True:
                answer += s[i].upper()
                checkUpper = False
            else:
                answer += s[i].lower()
                checkUpper = True
    return answer

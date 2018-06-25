def solution(s, n):
    minus1 = ord('z') - ord('a')
    minus2 = ord('Z') - ord('A')
    answer = ''
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
        elif ord('A') <= ord(s[i]) and ord(s[i]) <= ord('Z'):
            if ord(s[i]) + n > ord('Z'):
                temp = ord(s[i]) + n - minus2 - 1
                answer += chr(temp)
            else:
                temp = ord(s[i]) + n
                answer += chr(temp)
        else:
            if ord(s[i]) + n > ord('z'):
                temp = ord(s[i]) + n - minus1 - 1
                answer += chr(temp)
            else:
                temp = ord(s[i]) + n
                answer += chr(temp)
    return answer

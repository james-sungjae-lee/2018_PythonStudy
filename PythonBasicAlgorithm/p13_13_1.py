# -*- coding: utf-8 -*-
# 큐와 스택을 이용하지 않고 주어진 문장이 회문인지 아닌지 찾기
# 입력 : 문자열 s
# 출력 : 회문이면 True, 아니면 False

def palindrome_without(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i].isalpha() == False:
            i += 1
        elif s[j].isalpha() == False:
            j -= 1
        elif s[i].lower() != s[j].lower():
            return False
        else:
            i += 1
            j -= 1

    return True

print(palindrome_without("Wow"))
print(palindrome_without("Madam, I'm Adam."))
print(palindrome_without("Madam, I am Adam."))
print(palindrome_without("KAAA"))

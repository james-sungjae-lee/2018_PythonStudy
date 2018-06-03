# -*- coding: utf-8 -*-
# 큐와 스택을 이용하지 않고 주어진 문장이 회문인지 아닌지 찾기
# 입력 : 문자열 s
# 출력 : 회문이면 True, 아니면 False

def palindrome_without(s):
    a = []
    for x in s:
        if x.isalpha():
            a.append(x.lower())

    while len(a) == 1:
        if a.pop[0] != a.pop[-1]:
            return False

    return True

print(palindrome_without("Wow"))
print(palindrome_without("Madam, I'm Adam."))
print(palindrome_without("Madam, I am Adam."))
print(palindrome_without("KAAA"))

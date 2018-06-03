# -*- coding: utf-8 -*-

import math

def squareSum_n(n):
    s = 0;
    for i in range(1, n+1):
        s = s + (i*i)
    return s

print(squareSum_n(10))
print(squareSum_n(20))


# 1부터 n까지 연속한 숫자의 제곱의 합을 구하는 프로그램을 for 반복문으로 만들어 보세요
# 예를 들어 n = 10이라면 1제곱 + 2제곱 + ... + 10 제곱 = 385를 계산하는 프로그램입니다.

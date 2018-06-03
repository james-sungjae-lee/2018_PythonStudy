# -*- coding: utf-8 -*-

#1부터 n까지 연속한 숫자의 제곱의 합을 구하는 공식은 n(n+1)(2n+1)/6 입니다.
#for 반복문 대신 이 공식을 이용하면 알고리즘의 계산 복잡도는 O(1)과 O(n)중 무엇일까요?
#-> n의 크기와 상관없이 5회 연산하므로 O(1) 의 복잡도를 가진다.

import math

def squareSumEasy_n(n):
    s = n*(n+1)*((2*n)+1)//6
    return s

print(squareSumEasy_n(10))

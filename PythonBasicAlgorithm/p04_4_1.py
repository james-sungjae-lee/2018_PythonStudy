# -*- coding: utf-8 -*-
# 문제 1의 1부터 n까지의 합 구하기를 재귀 호출로 만들어 보세요

def sum(n):
    if n <= 0:
        return 0
    return n + sum(n-1)

print(sum(10))
print(sum(100))

# def fact(n):
#     if n <= 1:
#         return 1
#     return n * fact(n-1)

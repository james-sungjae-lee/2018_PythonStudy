# -*- coding: utf-8 -*-
# 문제 2의 숫자 n개 중에서 최댓값 찾기를 재귀 호출로 만들어 보시오.

def find_max(a,n):
    if n == 1:
        return a[0]
    max_v = find_max(a, n-1)
    if max_v > a[n-1]:
        return max_v
    else:
        return a[n-1]

v = [17, 92, 102, 40, 1923, 1230, 140]
print(find_max(v, len(v)))

# def find_max(a):
#     x = len(a) - 1
#     max_v = a[n]
#     if n <= 0:
#         return
#
#     if a[n] <= a[n-1]:
#         max_v = a[n-1]
#     return find_max(n-1)
#
# v = [17, 92, 102, 40, 1923, 1230, 140]
# print(find_max(v))

# v = [17, 92, 102, 40, 1923, 1230, 140]
# print(find_max(v))
#
# def find_max(a):
#     n = len(a)
#     max_v = 0
#     if n<=0:
#         return 0
#     return find_max()

# def sum(n):
#     if n <= 0:
#         return 0
#     return n + sum(n-1)
#
# print(sum(10))
# print(sum(100))

# def find_max(a):
#     n = len(a)
#     max_v = a[0]
#     for i in range(1, n):
#         if a[i] > max_v:
#             max_v = a[i]
#     return max_v
#
# v = [17, 92, 102, 40, 1923, 1230, 140]
# print(find_max(v))

# def find_max_idx(a):
#     n = len(a)
#     max_idx = 0
#     for i in range(1, n):
#         if a[i] > a[max_idx]:
#             max_idx = i
#
#     return max_idx
#
# v = [17, 92, 102, 40, 1923, 1230, 140]
# print(find_max_idx(v))

# def fact(n):
#     if n <= 1:
#         return 1
#     return n * fact(n-1)

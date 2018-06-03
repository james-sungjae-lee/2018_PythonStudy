# -*- coding: utf-8 -*-

# 최솟값 구하기
# 입력 : 숫자가 n개 들어 있는 리스트
# 출력 : 숫자 n개 중 최솟값
# 최솟값의 위치 번호를 구하기

def find_min_idx(a):
    n = len(a)
    min_idx = 0
    for i in range(1, n):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx

v = [17, 92, 102, 40, 1923, 10, 1230, 140]
print(find_min_idx(v))
print(v[find_min_idx(v)])

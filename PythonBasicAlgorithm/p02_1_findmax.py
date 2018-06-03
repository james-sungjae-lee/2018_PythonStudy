# -*- coding: utf-8 -*-

#최댓값 구하기
# 입력 : 숫자가 n개 들어 있는 리스트
# 출력 : 숫자 n개 중 최댓값

def find_max(a):
    n = len(a)
    max_v = a[0]
    for i in range(1, n):
        if a[i] > max_v:
            max_v = a[i]
    return max_v

v = [17, 92, 102, 40, 1923, 1230, 140]
print(find_max(v))

# 복잡도에 대하여
# 1개씩 비교하여 최댓값 n횟수만큼 반복하므로 O(n)의 복잡도를 가진다.

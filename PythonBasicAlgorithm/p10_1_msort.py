# -*- coding: utf-8 -*-
# 쉽게 설명한 병합 정렬
# 입력 : 리스트 a
# 출력 : 정렬된 새 리스트

def merge_sort(a):
    n = len(a)
    # 종료 조건 : 정렬 리스트의 자료 개수가 한 개 이하.
    if n <= 1:
        return a
    # 그룹을 나누어 각각 병합 정렬을 호출

    mid = n // 2 # 중간을 기준으로 두 그룹으로 나눔
    g1 = merge_sort(a[:mid]) # 재귀 호출로 첫 번째 그룹을 정렬
    g2 = merge_sort(a[mid:]) # 재귀 호출로 두 번째 그룹을 정렬

    # 두 그룹을 하나로 병합

    result = []
    while g1 and g2:
        if g1[0] < g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))

    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))
    return result

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(merge_sort(d))

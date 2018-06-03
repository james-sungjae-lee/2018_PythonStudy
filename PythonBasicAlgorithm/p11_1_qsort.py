# -*- coding: utf-8 -*-
# 쉽게 설명한 퀵 정렬
# 입력 : 리스트 a
# 출력 : 정렬된 새 리스트

def quick_sort(a):
    n = len(a)
    # 종료 조건 : 정렬할 리스트의 자료 개수가 한 개 이하이면 정렬할 필요가 없다.
    if n <= 1:
        return a
    # 기준 값을 정하고 기준에 맞춰 그룹을 나누는 과정
    pivot = a[-1]
    g1 = []
    g2 = []
    for i in range(0, n-1):
        if a[i] < pivot:
            g1.append(a[i])
        else:
            g2.append(a[i])
        print(pivot)
        print(g1)
        print(g2)

    # 각 그룹에 대해 재귀호출로 퀵정렬
    # 기준 값과 합쳐 하나의 리스트로 결괏값 반환
    return quick_sort(g1) + [pivot] + quick_sort(g2)

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(quick_sort(d))

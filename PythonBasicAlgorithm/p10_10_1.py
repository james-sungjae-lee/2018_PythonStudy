# -*- coding: utf-8 -*-
# 일반적인 병합 정렬 // 내림차순으로 바꾸시오
# 입력 : 리스트 a
# 출력 : 없음
# 분할 정복 / 계산 복잡도 : O(n * log_n)

def merge_sort(a):
    n = len(a)
    # 종료 조건 : 정렬할 리스트의 자료 개수가 한 개 이하
    if n <= 1:
        return
    # 그룹을 나누어 각각 병합 정렬을 호출하기

    mid = n // 2
    g1 = a[:mid]
    g2 = a[mid:]
    merge_sort(g1)
    merge_sort(g2)

    # 두 그룹을 하나로 병합
    i1 = 0
    i2 = 0
    ia = 0
    while i1 < len(g1) and i2 < len(g2):
        if g1[i1] > g2[i2]: # 이곳의 부등호를 바꿔준다. 그 외에는 건드릴게 없다.
            a[ia] = g1[i1]
            i1 += 1
            ia += 1
        else:
            a[ia] = g2[i2]
            i2 += 1
            ia += 1

    # 아직 남은 자료들을 결과에 추가
    while i1 < len(g1):
        a[ia] = g1[i1]
        i1 += 1
        ia += 1
    while i2 < len(g2):
        a[ia] = g2[i2]
        i2 += 1
        ia += 1
    print(g1)
    print(g2)

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5, 8, 3, 9, 10, 1, 2, 4, 7, 5, 8, 3, 9, 10, 1, 2, 4, 7, 5]
merge_sort(d)
print(d)

# -*- coding: utf-8 -*-
# 일반적인 버블 정렬
# 입력 : 리스트 a
# 출력 : 없음

def bubble_sort(a):
    n = len(a)
    while True:
        changed = False
        for i in range(0, n-1):
            if a[i] > a[i + 1]:
                print(a)
                a[i], a[i + 1] = a[i + 1], a[i]
                changed = True
                if changed == False:
                    return
e = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
bubble_sort(e)
print(e)

# def bubble_sort(a):
#     n = len(a)
#     for i in range(0, n - 1):
#         if a[i] > a[i + 1]:
#             a[i], a[i + 1] = a[i + 1], a[i]
#         else:
#             return a
#         print(a)
#     return bubble_sort()

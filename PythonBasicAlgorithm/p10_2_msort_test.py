# -*- coding: utf-8 -*-

def merge_sort(a):
    n = len(a)
    if n <= 1:
        return

    mid = 0 # << 이곳에서 나눌 위치를 정해준다. a[mid] 가 위치의 실제값이 된다.
    g1 = a[:mid] # << 위치값을 기준으로, 위치값을 제외한 앞의 값들이 들어간다.
    g2 = a[mid:] # << 위치값을 기준으로, 위치값을 포함한 뒤의 값들이 들어간다.

    print(g1)
    print(g2)

v = [1, 2, 3, 4, 5, 6, 7,]
merge_sort(v)
print(v)

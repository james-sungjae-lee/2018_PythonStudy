# -*- coding: utf-8 -*-
# 큰 수에서 작은 수로 정렬되도록 바꾸려면 어떻게 해야 할까?
# 방법 1. 최솟값이 아닌, 최댓값을 구해 앞에서부터 넣는다. OK

def find_max_idx(a):
    n = len(a)
    max_idx = 0
    for i in range(1, n):
        if a[i] > a[max_idx]:
            max_idx = i
    return max_idx

def sel_sort(a):
    result = []
    while a:
        max_idx = find_max_idx(a)
        value = a.pop(max_idx)
        result.append(value)
    return result

d = [2, 4, 5, 1, 3]
e = [2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3]

print(sel_sort(d))
print(sel_sort(e))

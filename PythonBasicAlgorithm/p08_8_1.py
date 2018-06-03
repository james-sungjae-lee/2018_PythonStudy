# -*- coding: utf-8 -*-
# 1. 선택정렬 함수를 정의내린다.
# 2. 값을 출력할 빈 리스트를 하나 만든다.
# 3. while 문을 사용해 입력받은 리스트가 빈 리스트가 될 때까지 값을 하나씩 빼오도록 한다.
# 4. 이 때, 빼오는 값이 그 리스트의 최솟값이 되도록 최솟값을 구하는 함수를 하나 만든다.
# 5. 최솟값을 하나 빼오는 데 성공했다면, 새롭게 만든 빈 리스트에 0의 위치부터 차곡차곡 쌓는다.
# 6. 새롭게 만들어진 리스트는 정렬 된 리스트이며, 이를 출력한다.

def find_min_idx(a):
    n = len(a)
    min_idx = 0
    for i in range(1, n):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx

def sel_sort(a):
    result = []
    while a:
        min_idx = find_min_idx(a)
        value = a.pop(min_idx)
        result.append(value)
    return result

d = [2, 4, 5, 1, 3]
e = [2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3]

print(sel_sort(d))
print(sel_sort(e))

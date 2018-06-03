# -*- coding: utf-8 -*-
# 책의 테스트를 따라해보기
# 입력 : 리스트 a
# 출력 : 정렬된 새 리스트

# 리스트 r에서 v가 들어가야 할 위치를 돌려주는 함수

def find_ins_idx(r, v):
    for i in range(0, len(r)):
        if v < r[i]:
            return i
    return len(r)

def ins_sort(a):
    result = []
    while a :
        value = a.pop(0)
        ins_idx = find_ins_idx(result, value)
        result.insert(ins_idx, value)
        print(a, result)
    return result

d = [2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3, 2, 4, 5, 1, 3]
print(ins_sort(d))

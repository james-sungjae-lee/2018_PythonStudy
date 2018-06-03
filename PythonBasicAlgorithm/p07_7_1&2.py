# -*- coding: utf-8 -*-
# 리스트에서 특정 숫자의 위치 찾기
# 입력 : 리스트 a, 찾는 값 x
# 출력 : 찾으면 그 값의 위치들을 리스트로 저장 후 출력, 찾지 못하면 []

def search_list_upgrade(a, x):
    n = len(a)
    result = set()
    for i in range(0, n):
        if x == a[i]:
            result.add(i)
    return result

v = [17, 92, 18, 33, 58, 7, 33, 42, 17, 92, 18, 33, 58, 7, 33, 42]

print(search_list_upgrade(v, 18))
print(search_list_upgrade(v, 33))
print(search_list_upgrade(v, 900))

# 7-2
# 7-1의 프로그램 계산 복잡도는 무엇일까요
# 동일하게 O(n)이다.

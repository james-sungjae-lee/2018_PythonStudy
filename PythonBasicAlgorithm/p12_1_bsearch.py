# -*- coding: utf-8 -*-
# 리스트에서 특정 숫자 위치 찾기 (이분 탐색 )
# 입력 : 리스트 a / 찾는 값 x
# 출력 : 찾으면 그 값의 위치 / 찾지 못하면 -1

def binary_search(a, x):
    # 탐색 범위의 저장 변수 start / end
    # 리스트 전체를 범위로 탐색 시작 (0 ~ len(a) -1)

    start = 0
    end = len(a) - 1
    print(a)
    print("Let's search", x, " value")

    while start <= end:
        mid = (start + end) // 2
        print(a[start], a[mid], a[end]) # 참고용 코드

        if x == a[mid]: # 찾는 값을 발견하면
            return mid

        elif x > a[mid]: # 찾는 값이 중간값보다 크면
            start = mid + 1 # start 에 중간값 + 1 을 넣고 다시 탐색

        else: # 찾는 값이 중간값보다 작으면
            end = mid - 1 # end 에 중간값 - 1 을 넣고 다시 탐색

        print(a[start], a[end]) # 참고용 코드
        print()

    return -1 # 찾지 못했을 경우

d = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(binary_search(d, 36))
print(binary_search(d, 50))

# -*- coding: utf-8 -*-
# 주어진 동전 n개 중에 가짜 동전 fake 를 찾아내는 알고리즘
# 입력 : 전체 동전 위치의 시작과 끝 (0, n - 1)
# 출력 : 가짜 동전의 위치 번호

# 무게 재기 함수
# a에서 b까지에 놓인 동전과
# c에서 d까지에 놓인 동전의 무게를 비교
# a에서 b까지에 가짜 동전이 있다면 -1
# c에서 d까지에 가짜 동전이 있다면 1
# 없다면 0

def weigh(a, b, c, d):
    fake = 90 # 가짜 동전의 실제 위치
    if a <= fake and fake <= b:
        return -1
    if c <= fake and fake <= d:
        return 1
    return 0

# weigh()를 이용하여
# left 에서 right까지 놓인 가짜 동전의 위치를 찾아냄

def find_fakecoin(left, right):
    if left == right: # 가짜 동전이 있을 범위에 동전이 한 개 뿐이면 ( 양쪽 끝값이 같으면 ) 그 동전이 가짜동전이다.
        return left
    # left 에서 right 까지 놓인 동전을 g1_left ~ g1_right / g2_left ~ g2 right 로 나눈다.
    # 동전 수가 홀수면 두 그룹으로 나누고 한 개가 남는다.
    half = (right - left + 1) // 2
    g1_left = left
    g1_right = left + half - 1
    g2_left = left + half
    g2_right = g2_left + half - 1

    # 나눠진 두 그룹을 weigh()로 저울질
    result = weigh(g1_left, g1_right, g2_left, g2_right)
    if result == -1: #그룹 1이 가벼우면
        print("왼쪽")
        return find_fakecoin(g1_left, g1_right)
    elif result == 1: #그룹 2가 가벼우면
        print("오른쪽")
        return find_fakecoin(g2_left, g2_right)
    else:
        return right # 남은 한 개가 가짜임


n = 10000
print(find_fakecoin(0, n-1))

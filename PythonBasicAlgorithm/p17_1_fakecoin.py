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
    fake = 4 # 가짜 동전의 실제 위치
    if a <= fake and fake <= b:
        return -1
    if c <= fake and fake <= d:
        return 1
    return 0

# weigh()를 이용하여
# left 에서 right까지 놓인 가짜 동전의 위치를 찾아냄

def find_fakecoin(left, right):
    for i in range(left + 1, right + 1):
        # 가장 왼쪽 동전과 나머지 동전을 차례로 비교
        result = weigh(left, left, i, i)
        if result == -1:
            return left
        elif result == 1:
            return i
        print(result) # 확인 코드
    return -1

n = 30
print(find_fakecoin(0, n-1))

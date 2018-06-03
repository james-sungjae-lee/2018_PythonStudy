# -*- coding: utf-8 -*-
# 최대 수익 문제를 푸는 두 알고리즘의 계산 속도 비교하기
# 최대 수익 문제를 O(n*n)과 O(n)으로 푸는 알고리즘을 각각 수행하여
# 걸린 시간을 출력 / 비교함

import time # 시간 측정을 위한 time 모듈
import random # 테스트 주가 생성을 위한 random 모듈

# 최대 수익 : 느린 O(n*n) 알고리즘
def max_profit_slow(prices):
    n = len(prices)
    max_profit = 0

    for i in range(0, n - 1):
        for j in range( i + 1 , n ):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
    return max_profit

def max_profit_fast(prices):
    n = len(prices)
    max_profit = 0
    min_price = prices[0]

    for i in range(1, n):
            profit = prices[i] - min_price
            if profit > max_profit:
                max_profit = profit
            if prices[i] < min_price:
                min_price = prices[i]
    return max_profit



def test(n):
    # 테스트 자료 만들기 (5000 부터 20000의 난수를 주가로 사용)
    a = []
    for i in range(0, n):
        a.append(random.randint(5000, 20000))
    # 느린 알고리즘 테스트
    start = time.time()
    mps = max_profit_slow(a)
    end = time.time()
    time_slow = end - start

    # 빠른 알고리즘 테스트
    start = time.time()
    mpf = max_profit_fast(a)
    end = time.time()
    time_fast = end - start

    #결과 출력 : 계산결과 비교
    print(n, mps, mpf) # 입력 크기, 각각 알고리즘이 계산한 최대 수익 값

    #결과 출력 : 계산시간 비교
    m = 0 # 느린 알고리즘과 빠른 알고리즘의 수행 시간 비율의 저장
    if time_fast > 0:
        m = time_slow / time_fast

    print("%d %.5f %.5f %.2f" % (n, time_slow, time_fast, m))

test(100)
test(10000)
test(30000)

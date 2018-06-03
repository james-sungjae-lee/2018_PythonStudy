# -*- coding: utf-8 -*-
# 주어진 주식 가격을 보고 최대 수익을 구하는 알고리즘
# 입력 : 주식 가격의 변화 값 / 리스트 : price
# 출력 : 한 주를 한 번 사고팔아 얻을 수 있는 최대 수익 값

def max_profit(prices):
    n  = len(prices)
    max_profit = 0 # 최대 수익은 항상 0 이상
    min_price = prices[0] # 9600 /

    for i in range(1, n): # 1 부터 n - 1 까지 반복
            print(prices[i]) ## 참고 코드
            # 지금까지의 최솟값에 주식을 사서 i날에 팔았을 때 얻는 수익
            profit = prices[i] - min_price
            # 이 수익이 지금까지의 최대 수익보다 크면, 값을 고친다.
            if profit > max_profit:
                max_profit = profit
            if prices[i] < min_price:
                min_price = prices[i]
            print(profit) ## 참고 코드
            print(min_price)
            print

    return max_profit

stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
print(max_profit(stock))

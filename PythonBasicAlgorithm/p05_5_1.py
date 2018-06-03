# -*- coding: utf-8 -*-
# 0과 1부터 시작해서 바로 앞의 두 수를 더한 값을 다음 값으로 추가하는 방식의 수열을
# 피보나치 수열이라고 한다.
# 즉, 0 + 1 = 1, 1 + 1 = 2, 1 + 2 = 3, 3 + 2 = 6... = 0, 1, 1, 2, 3, 6...
# 피보나치 수열이 파이썬의 리스트처럼 0번부터 시작한다고 할 때, n번째 피보나치 수를 구하는 알고리즘을
# 재귀호출을 이용해서 구현해 보시오

def fibonacci_n(n):
    if n <= 1:
        return n
    return fibonacci_n(n-2) + fibonacci_n(n-1)

print(fibonacci_n(10))
print(fibonacci_n(7))

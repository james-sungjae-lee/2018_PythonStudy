def solution(n):
    answer = 0
    for i in range(n + 1):
        if i != 0 and n % i == 0:
            answer += i
    return answer

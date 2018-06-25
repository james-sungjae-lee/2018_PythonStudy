def solution(s):
    answer = list(s)
    if answer[0] == '-':
        answer = answer[1:]
        minus = True
    elif answer[0] == '+':
        answer = answer[1:]
        minus = False
    else:
        minus = False
    answer = list(map(int, answer))
    answer.reverse()
    result = 0
    time = 1
    for i in answer:
        result += i * time
        time *= 10
    if minus == True:
        result *= -1
    return result

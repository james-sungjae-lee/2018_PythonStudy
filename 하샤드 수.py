def solution(x):
    x_list = list(str(x))
    sum_x = 0
    for i in x_list:
        sum_x += int(i)
    if x % sum_x is 0:
        answer = True
    else:
        answer = False
    return answer

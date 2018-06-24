def solution(a, b):
    result = 0
    if a > b:
        temp = a
        a = b
        b = temp
    for i in range(a, b + 1):
        result += i
    return result

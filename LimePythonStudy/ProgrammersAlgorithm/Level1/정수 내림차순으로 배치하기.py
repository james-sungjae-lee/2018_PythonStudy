def solution(n):
    data = list(str(n))
    data.sort()
    result = 0
    time = 1
    for i in data:
        result += int(i) * time
        time *= 10
    return result

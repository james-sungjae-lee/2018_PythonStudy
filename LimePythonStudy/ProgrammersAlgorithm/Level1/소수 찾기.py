def solution(n):
    answer = 0
    for i in range(2, n+1):
        if checkPrime(i) is True:
            answer += 1
    return answer

def checkPrime(n):
    if n < 2:
        return False
    if n is 2:
        return True
    if n % 2 is 0:
        return False
    x = round(n**0.5) + 1
    for i in range(3, x, 2):
        if n % i is 0:
            return False
    return True


    

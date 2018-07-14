def solution(n):
    answer = 0
    for i in range(1,n+1):
        check = 0
        j = i
        while( check <= n):
            check += j
            j += 1
            if check == n:
                answer += 1
    return answer

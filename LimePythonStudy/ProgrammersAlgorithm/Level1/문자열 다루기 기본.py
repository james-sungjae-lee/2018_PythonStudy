def solution(s):
    check = True
    for i in s:
        if i.isalpha():
            check = False
    return (len(s) == 4 or len(s) == 6)and(check)

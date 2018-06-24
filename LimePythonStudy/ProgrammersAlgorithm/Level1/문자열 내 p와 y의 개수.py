def solution(s):
    numOfP = 0
    numOfY = 0
    for i in s:
        if(i == 'y' or i == 'Y'):
            numOfY += 1
        if(i == 'p' or i == 'P'):
            numOfP += 1
    if numOfP == numOfY:
        return True
    else:
        return False

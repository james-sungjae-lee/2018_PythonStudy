def solution(s):
    answer = ''
    s_list = s.split(' ')
    answer_list = []
    for i in s_list:
        answer_list.append(int(i))
    answer = str(min(answer_list)) + ' ' + str(max(answer_list))
    return answer

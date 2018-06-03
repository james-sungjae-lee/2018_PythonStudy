# -*- coding: utf-8 -*-
# 학생 번호로 학생 이름을 찾는 문제
# 학생 번호와 이름이 주어졌을 때, 학생 번호를 입력하면 그 학생 번호에 해당하는 이름을 출력
# 해당 학생 번호가 없으면 물음표를 출력

def find_name(s_info, find_number):
    for i in range(0, len(s_info)):
        if find_number in s_info: # 이해되지 않음!
            return s_info[find_number]
        else:
            return "?"

sample_data = {
    39 : "Justin",
    14 : "Jhon",
    67 : "Mike",
    105: "Summer"
}

print(find_name(sample_data, 105))

# -*- coding: utf-8 -*-
# 다음과 같이 학생 번호와 이름이 리스트로 주어졌을 때, 학생 번호를 입력하면 학생 번호에 해당하는 이름을
# 순차 탐색으로 찾아 돌려주는 함수를 만들어 보시오.
# 해당하는 학생 번호가 없으면 물음표 "?"를 돌려준다.
#
# 입력 : 학생 번호 리스트 a, 학생 이름 리스트 b, 찾는 값 x
# 출력 : 찾으면 그 값의 위치(학생 번호로 수정), 그리고 값(학생 이름)을 출력 / 찾지 못하면 "?" 출력

def search_student_list(a, b, x):
    n = len(a)
    for i in range(0, n):
        if x == a[i]:
            return b[i]
    return "?"

stu_no = [39, 14, 67, 105, 999]
stu_name = ["Justin", "John", "Mike", "Summer", "A"]

print(search_student_list(stu_no, stu_name, 0))
print(search_student_list(stu_no, stu_name, 105))
print(search_student_list(stu_no, stu_name, 999))
print(search_student_list(stu_no, stu_name, 14))
print(search_student_list(stu_no, stu_name, 39))
print(search_student_list(stu_no, stu_name, 88))

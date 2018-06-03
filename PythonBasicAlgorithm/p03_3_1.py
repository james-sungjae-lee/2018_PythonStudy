# -*- coding: utf-8 -*-

#n명 중 두 명을 뽑아 짝을 짓는다고 할 때,
#짝을 지을 수 있는 모든 조합을 출력하는 알고리즘을 만드시오
#예를 들어 "Tom", "Jerry", "Mike" 라면 Tom - Jerry / Tom - Mike / Jerry - Mike

def bindPerson(a):
    n = len(a)
    for i in range(0, n-1):
        for j in range(i+1, n):
            if a[i] != a[j]:
                print(a[i],"-", a[j])
name = ["A", "B", "C", "D", "E", "F"]
print(bindPerson(name))

# def bindPerson(a):
#     n = len(a)
#     result = set()
#     for i in range(0, n-1):
#         for j in range(i-1, n):
#             if a[i] != j[i]:
#                 result.add(a[i],a[j])
#     return result
#
# name = ["Tom", "Jerry", "Mike"]
# print(bindPerson(name))

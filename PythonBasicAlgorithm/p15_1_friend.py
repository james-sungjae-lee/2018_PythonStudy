# -*- coding: utf-8 -*-
# 친구 리스트에서 자신의 모든 친구를 찾는 알고리즘
# 입력 : 친구 관계 그래프 g, 모든 친구를 찾을 자신 start
# 출력 : 모든 친구의 이름

def print_all_friends(g, start):
    qu = []
    done = set()

    qu.append(start) # 리스트에는 append
    done.add(start) # 집합에는 add 를 사용한다. 시작값 넣기.

    while qu:
        p = qu.pop(0)
        print(p)
        for x in g[p]: # p 의 그룹들(친구들)을 하나씩 빼내는 것.
            if x not in done: # 만약 뽑아낸 x가 done에 없을 경우
                qu.append(x) # qu 에 x 를 추가
                done.add(x) # done 에도 x 를 추가.

# 친구 관계 리스트
# A 와 B 가 친구이면
# A의 친구 리스트에도 B 가 나오고, B의 친구 리스트에도 A가 나옴

fr_info = {
    'Summer' : ['John', 'Justin', 'Mike'],
    'John' : ['Summer', 'Justin'],
    'Justin' : ['John', 'Summer', 'Mike', 'May'],
    'Mike' : ['Summer', 'Justin'],
    'May' : ['Justin', 'Kim'],
    'Kim' : ['May'],
    'Tom' : ['Jerry'],
    'Jerry' : ['Tom']
}

print_all_friends(fr_info, 'Summer')
print
print_all_friends(fr_info, 'Jerry')

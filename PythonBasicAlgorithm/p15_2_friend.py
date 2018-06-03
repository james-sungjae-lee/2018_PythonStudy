# -*- coding: utf-8 -*-
# 친구 리스트에서 자신의 모든 친구를 찾고, 친구들의 친밀도를 계산하는 알고리즘
# 입력 : 친구 관계 그래프 g, 모든 친구를 찾을 자신 start
# 출력 : 모든 친구의 이름과 친밀도

def print_all_friends(g, start):
    qu = [] # 기억 장소 1 : 앞으로 처리해야 할 (사람 이름, 친밀도) 튜플을 큐에 저장
    done = set() # 기억 장소 2 : 이미 큐에 추가한 사람을 집합에 기록 (중복 방지)

    qu.append((start, 0)) # (사람 이름, 친밀도) 정보를 하나의 튜플로 묶어 처리한다.

    done.add(start) # 집합에는 add 를 사용한다. 시작값 넣기.

    while qu:
        (p, d) = qu.pop(0)
        print(p, d)
        for x in g[p]: # p 의 그룹들(친구들)을 하나씩 빼내는 것.
            if x not in done: # 만약 뽑아낸 x가 done에 없을 경우
                qu.append((x, d + 1)) # qu 에 x 를 추가, d를 하나 증가시켜 추가
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

# -*- coding: utf-8 -*-
# 15에서 배운 그래프 탐색 알고리즘을 이용하여 다음 그래프를 탐색하는 프로그램을 만들어 보시오
# 1 - 3 / 1 - 2 / 2 - 4 / 2 - 5

def graph_search(g, start):
    qu = []
    done = set()

    qu.append(start)

    done.add(start)

    while qu:
        p = qu.pop(0)
        print(p)
        for x in g[p]:
            if x not in done:
                qu.append(x)
                done.add(x)

graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}

graph_search(graph, 3)

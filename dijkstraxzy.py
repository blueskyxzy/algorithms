#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from datetime import datetime

# Dijkstra算法
# 算法特点：
# 迪科斯彻算法使用了广度优先搜索解决赋权有向图或者无向图的单源最短路径问题，算法最终得到一个最短路径树。该算法常用于路由算法或者作为其他图算法的一个子模块。
#
# 算法的思路:
# Dijkstra算法采用的是一种贪心的策略，声明一个数组dis来保存源点到各个顶点的最短距离和一个保存已经找到了最短路径的顶点的集合：T，初始时，原点 s 的路径权重被赋为 0 （dis[s] = 0）。
# 若对于顶点 s 存在能直接到达的边（s,m），则把dis[m]设为w（s, m）,同时把所有其他（s不能直接到达的）顶点的路径长度设为无穷大。初始时，集合T只有顶点s。
# 然后，从dis数组选择最小值，则该值就是源点s到该值对应的顶点的最短路径，并且把该点加入到T中，OK，此时完成一个顶点，
# 然后，我们需要看看新加入的顶点是否可以到达其他顶点并且看看通过该顶点到达其他点的路径长度是否比源点直接到达短，如果是，那么就替换这些顶点在dis中的值。
# 然后，又从dis中找出最小值，重复上述动作，直到T中包含了图的所有顶点。

# 个人理解
# 需要2个数组，1个dis记录顶点到各节点的当前的最短路径，1个T代表当前已经决定最短路径的订点
# 初始化的时候，dis全部是inf,T为空，然后为顶点vo
# 开始从vo的路径来更新dis最短路径，找出最dis中找到不是T中顶点的最小的那个路径的订单就是确定的最短的路径和顶点了
# 遍历刚才确定最短路径的顶点的路径，更新dis和T,这样重复至所有顶点，dis就是最终的顶点到各节点的最短路径
# 实质还是遍历所有的路径，统计最短的路径值，从已确定的最短路径节点来找最小的最短路径作为确定的节点

# 初始化图参数
G = {1: {1: 0, 2: 1,  3: 12},
     2: {2: 0, 3: 9,  4: 3},
     3: {3: 0, 5: 5},
     4: {3: 4, 4: 0,  5: 13, 6: 15},
     5: {5: 0, 6: 4},
     6: {6: 0}}


def dijkstraxzy(G, v0):
    # vo表示顶点 s
    v = v0
    T = set()
    dis = dict((i, float("inf")) for i in G.keys())     # !!!!!!
    dis[1] = 0
    while len(T) < len(G):                      # 确定顶点的个数等于所有顶点就结束
        T.add(v)                                # 确定最短路径的顶点
        for j in G[v]:                          # 遍历
            if G[v][j] + dis[v] < dis[j]:
                dis[j] = dis[v] + G[v][j]       # 更新最短路径

        min = float('inf')
        for k in dis:                             # 找出dis中非T中的最小路径值
            if k in T:
                continue
            if dis[k] < min:
                min = dis[k]
                v = k

    return dis



time1 = datetime.now()
dis = dijkstraxzy(G, v0 = 1)
time2 = datetime.now()
timeDef = (time2 - time1).microseconds   # 单位微秒
print("用时：" + str(timeDef) + "微妙")
print(dis)
print dis.values()
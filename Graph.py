#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# 首先有一个概念：回溯
#
# 回溯法(探索与回溯法)是一种选优搜索法，按选优条件向前搜索，以达到目标。但当探索到某一步时，发现原先选择并不优或达不到目标，就退回一步重新选择，这种走不通就退回再走的技术为回溯法，而满足回溯条件的某个状态的点称为“回溯点”。
#
# 深度优先算法：Depth First Search
#
# （1）访问初始顶点v并标记顶点v已访问。
# （2）查找顶点v的第一个邻接顶点w。
# （3）若顶点v的邻接顶点w存在，则继续执行；否则回溯到v，再找v的另外一个未访问过的邻接点。
# （4）若顶点w尚未被访问，则访问顶点w并标记顶点w为已访问。
# （5）继续查找顶点w的下一个邻接顶点wi，如果v取值wi转到步骤（3）。直到连通图中所有顶点全部访问过为止。
#
# 广度优先算法：Breadth First Search
#
# （1）顶点v入队列。
# （2）当队列非空时则继续执行，否则算法结束。
# （3）出队列取得队头顶点v；访问顶点v并标记顶点v已被访问。
# （4）查找顶点v的第一个邻接顶点col。
# （5）若v的邻接顶点col未被访问过的，则col入队列。
# （6）继续查找顶点v的另一个新的邻接顶点col，转到步骤（5）。直到顶点v的所有未被访问过的邻接点处理完。转到步骤（2）。

class Graph(object):

    def __init__(self, *args, **kwargs):
        self.node_neighbors = {}
        self.visited = {}

    def add_nodes(self, nodelist):

        for node in nodelist:
            self.add_node(node)

    def add_node(self, node):
        if node not in self.nodes():
            self.node_neighbors[node] = []

    def add_edge(self, edge):
        u, v = edge
        if(v not in self.node_neighbors[u]) and (u not in self.node_neighbors[v]):
            self.node_neighbors[u].append(v)
            if(u!=v):
                self.node_neighbors[v].append(u)

    def nodes(self):
        return self.node_neighbors.keys()

    def depth_first_search(self, root=None):
        order = []

        self.visited = {}
        def dfs(node):
            self.visited[node] = True
            order.append(node)
            for n in self.node_neighbors[node]:
                if not n in self.visited:
                    dfs(n)

        if root:
            dfs(root)

        for node in self.nodes():
            if not node in self.visited:
                dfs(node)

        print(order)
        return order

    def breadth_first_search(self, root=None):
        self.visited = {}
        queue = []
        order = []

        def bfs():
            while len(queue) > 0:
                node  = queue.pop(0)

                self.visited[node] = True
                for n in self.node_neighbors[node]:
                    if (not n in self.visited) and (not n in queue):
                        queue.append(n)
                        order.append(n)

        if root:
            queue.append(root)
            order.append(root)
            bfs()

        for node in self.nodes():
            if not node in self.visited:
                queue.append(node)
                order.append(node)
                bfs()
        print(order)

        return order


if __name__ == '__main__':
    g = Graph()
    g.add_nodes([i + 1 for i in range(8)])
    g.add_edge((1, 2))
    g.add_edge((1, 3))
    g.add_edge((2, 4))
    g.add_edge((2, 5))
    g.add_edge((4, 8))
    g.add_edge((5, 8))
    g.add_edge((3, 6))
    g.add_edge((3, 7))
    g.add_edge((6, 7))
    print("nodes:", g.nodes())
    order = g.breadth_first_search(1)
    order = g.depth_first_search(1)

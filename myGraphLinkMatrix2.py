# -*- coding: UTF-8 -*-
 
# 图的邻接矩阵
# 
#邻接矩阵表示法，用两个数组表示，一个一维数组和一个二维数组。
#一维数组存储节点信息，二维数组存储节点之间的关系。

class Graph:
    #初始化n*n矩阵，全置为0
    def __init__(self,vertex):
        self.vertex=vertex
        self.graph=[[0]*vertex for i in range(vertex)]

    def insert(self,u,v):
        #对存在连接关系的两个点，在矩阵里置1代表连接关系，0则无连接关系
        #无向图，连接关系是关于斜对角对称的
        self.graph[u-1][v-1]=1
        self.graph[v-1][u-1]=1
    def show(self):
        #展示图
        for i in self.graph:
            for j in i:
                print(j,end=' ')
            print(' ')
     
if __name__ == '__main__':
    graph = Graph(5)
    graph.insert(1, 4)
    graph.insert(4, 2)
    graph.insert(4, 5)
    graph.insert(2, 5)
    graph.insert(5, 3)
    graph.show()
    #DoTest()
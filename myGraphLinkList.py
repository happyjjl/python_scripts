# -*- coding: UTF-8 -*-
 
# 图的邻接表法
# 

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
    def addNeighbor(self, nbr, weight = 0):
        self.connectedTo[nbr] = weight
    def __str__(self):
        return str(self.id) + ' connectedTo ' + str([x.id for x in self.connectedTo])
    def getConnections(self):
        return self.connectedTo.keys
    def getId(self):
        return self.id
    def getWeight(self, nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    def getVertex(self, n):
        if n in self.numVertices:
            return self.vertList[n]
        else:
            return None
    def contains(self, n):
        return n in self.vertList
    def addEdge(self, f, t, cost = 0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
    def getVertices(self):
        return self.vertList.keys
    def __str__(self):
        mykeys = list(self.vertList.keys())
        myVerts = ''
        myConns = ''
        for v in mykeys:
            myVerts = myVerts + ' ' + str(v)
            myConns = myConns + str(self.vertList[v]) + '\n'
        return '图中有' + str(self.numVertices) + '个点：' + str.lstrip(myVerts) + '\n点的连接如下：\n' + myConns
    def __iter__(self):
        return iter(self.vertList.values())
    


if __name__ == "__main__":
    g = Graph()
    for i in range(4):
        g.addVertex(i)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(1, 0)
    g.addEdge(3, 2)
    g.addEdge(3, 1)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    #aa = g.vertList[0].getConnections()
    print(g)

   
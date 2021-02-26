# -*- coding: UTF-8 -*- 
# 
# Eulerian Path is a path in graph that visits every edge exactly once.
# Eulerian Cycle(Circuit) is an Eulerian Path which starts and ends on the same
# vertex.
#
# Fleury’s Algorithm:
# http://www.graph-magics.com/articles/euler.php


# for checking in graph has euler path or cycle
# input:
#   graph   linklist
# output:
#   1   eulerian cycle
#   2   eulerian path
def isEulerianGraph(graph):
    odd_degree_nodes = 0
    for key in graph:
        if len(graph[key]) % 2 == 1:
            odd_degree_nodes += 1
            start_node = key
    if odd_degree_nodes == 0:
        return 1, key          # last vertex
    if odd_degree_nodes == 2:
        return 2, start_node   # last odd vertex
    return 3, -1

def findEulerianByFleury(graph, start_node):
    myStack = []
    myPath = []
    cur_vertex = start_node

    edges = 0
    for key in graph:
        edges += len(graph[key])

    #while len(myPath) < edges // 2 + 1:
    i = 0
    while i < edges + 1:       # need to loop every vertex's neighbor
        if len(graph[cur_vertex]) == 0:
            myPath.append(cur_vertex)
            if len(myStack) > 0:
                cur_vertex = myStack.pop()
        else:
            myStack.append(cur_vertex)
            mytemp = cur_vertex
            cur_vertex = graph[cur_vertex][0]  # move to neighbor
            graph[cur_vertex].remove(mytemp)   # delete edge 
            graph[mytemp].remove(cur_vertex)   # delete edge
        i += 1
    return myPath

def testGraph(graph):
    check, start_node = isEulerianGraph(graph)
    if check == 3:
        print("graph is not Eulerian")
        return
    if check == 2:
        print("graph has a Euler path")
    if check == 1:
        print("graph has a Euler cycle")
    path = findEulerianByFleury(graph, start_node)
    str_path = [str(x) for x in path]
    print('->'.join(str_path))

def printGraph(graph):
    num_vertex = len(graph)
    i = 0
    for key in graph:
        i += len(graph[key])
    num_edges = i // 2
    print('graph has ' + str(num_vertex) + ' vertexs and ' + str(num_edges) + ' edges')
    print(graph)
if __name__ == "__main__":
    #邻接表存储图
    G1 = {
        1: [2, 3, 4],
        2: [1, 3],
        3: [1, 2],
        4: [1, 5],
        5: [4]
    }
    G2 = {
        1: [2, 4],
        2: [1, 3, 5],
        3: [2, 6],
        4: [1, 5, 7],
        5: [2, 4, 6, 8],
        6: [3, 5, 8, 9],
        7: [4, 8],
        8: [5, 6, 7, 9],
        9: [6, 8]
    }
    G3 = {
        1: [2, 6],
        2: [1, 7],
        3: [4, 8],
        4: [3, 9],
        5: [],
        6: [1, 7],
        7: [2, 6, 8, 12],
        8: [3, 7, 9, 13],
        9: [4, 8, 10, 14],
        10: [9, 15],
        11: [12, 16],
        12: [7, 11, 13, 17],
        13: [8, 12, 14, 18],
        14: [9, 13, 15, 19],
        15: [10, 14],
        16: [11, 17, 21],
        17: [12, 16, 18, 22],
        18: [13, 17, 19, 23],
        19: [14, 18, 20, 24],
        20: [19, 25],
        21: [16, 22],
        22: [17, 21, 23],
        23: [18, 22],
        24: [19, 25],
        25: [20, 24]
    }
    G4 = { # 5 * 5 矩阵
        1: [2, 6],
        2: [1, 3, 7],
        3: [2, 4, 8],
        4: [3, 5, 9],
        5: [4, 10],
        6: [1, 7, 11],
        7: [2, 6, 8, 12],
        8: [3, 7, 9, 13],
        9: [4, 8, 10, 14],
        10: [5, 9, 15],
        11: [6, 12, 16],
        12: [7, 11, 13, 17],
        13: [8, 12, 14, 18],
        14: [9, 13, 15, 19],
        15: [10, 14, 20],
        16: [11, 17, 21],
        17: [12, 16, 18, 22],
        18: [13, 17, 19, 23],
        19: [14, 18, 20, 24],
        20: [15, 19, 25],
        21: [16, 22],
        22: [17, 21, 23],
        23: [18, 22, 24],
        24: [19, 23, 25],
        25: [20, 24]
    }
    G5 = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 3],
        3: [1, 2]
    }
    G6 = {
        1: [2, 4],
        2: [1, 3, 5],
        3: [2, 6],
        4: [1, 5, 7],
        5: [2, 4, 6, 8],
        6: [3, 5, 9],
        7: [4, 8],
        8: [5, 7, 9],
        9: [6, 8]
    }

    printGraph(G3)
    testGraph(G3)

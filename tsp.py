# -*- coding: UTF-8 -*-
#
# 美国大联盟2020-2021第7题
#
# Python3 program to implement traveling salesman 
# problem using naive approach. 
from sys import maxsize 
from itertools import permutations
V = 5
 
# implementation of traveling Salesman Problem 
def travellingSalesmanProblem(graph, s): 
 
    # store all vertex apart from source vertex 
    vertex_name = ['B', 'A', 'C', 'D', 'E'] 
    vertex_index = [0, 1, 2, 3, 4] 

    # store minimum weight Hamiltonian Cycle 
    min_path = maxsize 
    route = []
    next_permutation=permutations(vertex_index)
    for i in next_permutation:
 
        # store current Path weight(cost) 
        current_pathweight = 0
 
        # compute current path weight 
        k = s 
        for j in i: 
            current_pathweight += graph[k][j] 
            k = j 
        current_pathweight += graph[k][s] 
 
        # update minimum 
        if current_pathweight < min_path:
            min_path = current_pathweight
            min_route = i
        #min_path = min(min_path, current_pathweight) 
    for x in min_route:
        route.append(vertex_name[x])
    route.append('B')     
    return (min_path, route)
 
 
# Driver Code 
if __name__ == "__main__": 
 
    # matrix representation of graph 
    #         B  A  C  D  E
    #       B 0  5  4  6  10
    #       A 5  0  8  11 20  
    #       C 4  8  0  9  8
    #       D 6  11 9  0  2
    #       E 10 20 8  2  0
    graph = [[0, 5, 4, 6, 10], 
             [5, 0, 8, 11, 20], 
             [4, 8, 0, 9, 8], 
             [6, 11, 9, 0, 2],
             [10, 20, 8, 2, 0]] 
    s = 0
    print(travellingSalesmanProblem(graph, s))
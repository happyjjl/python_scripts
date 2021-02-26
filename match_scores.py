# -*- coding: UTF-8 -*- 
#
# 模拟体育比赛的结果和比分：
#  
# score_type: 
#   1  football mode: 3, 1, 0
#   2  chinese chess mode: 2, 1, 0

# match_type:
#   1  单循环
#   2  淘汰赛，此时player_num必须为偶数
#
# 

import math
import itertools
from collections import defaultdict

def getScores(matchs):
    scores = {}
    for key, value in matchs.items():
        scores[key] = sum(value.values())
    return scores

def checkMatch(matchs):
    score_keys = []
    scores = getScores(matchs)
    if len(scores) != len(set(scores.values())):
        return False
    new_scores = sorted(scores.items(), key=lambda item:item[1], reverse=True)
    for x in new_scores:
        score_keys.append(x[0])

    notfound0 = 0
    notfound1 = 0
    notfound2 = 0
    if not 0 in matchs[score_keys[1]].values():
        notfound0 = 1
    if not 1 in matchs[score_keys[0]].values():
        notfound1 = 1
    if not 2 in matchs[score_keys[3]].values():
        notfound2 = 1
    if notfound0 and notfound1 and notfound2:
        return True

def makeMatchGraph(matchs, results, type):

    '''
    match_graph = {}
    for player in players:
        match_graph[player] = {}
    '''
    if type == 1:
        max_point = 3
    else:
        max_point = 2
    # 使用deaultdict()初始化字典，可以避免键不存在添加值的错误，从而实现动态二维字典
    match_graph = defaultdict(dict)

    for match, result in zip(matchs, results):
        if result == 'tie':
            match_graph[match[0]][match[1]] = 1
            match_graph[match[1]][match[0]] = 1
        if result == 'win':
            match_graph[match[0]][match[1]] = max_point
            match_graph[match[1]][match[0]] = 0 
        if result == 'lose':
            match_graph[match[0]][match[1]] = 0
            match_graph[match[1]][match[0]] = max_point
    return match_graph

if __name__ == "__main__":
    
    G7 = {
        'A': {'B': 3, 'C': 3},
        'B': {'A': 0, 'C': 0},
        'C': {'A': 0, 'B': 3}
    }

    G8 = {
        'A': {'B': 2, 'C': 2, 'D': 2, 'E': 0}, 
        'B': {'A': 0, 'C': 1, 'D': 1, 'E': 1}, 
        'C': {'A': 0, 'B': 1, 'D': 2, 'E': 1}, 
        'D': {'A': 0, 'B': 1, 'C': 0, 'E': 1}, 
        'E': {'A': 2, 'B': 1, 'C': 1, 'D': 1}
    }
    G9 = {
        'C': {'A': 0, 'B': 1, 'D': 2, 'E': 1},
        'B': {'A': 0, 'C': 1, 'D': 1, 'E': 1},  
        'D': {'A': 0, 'B': 1, 'C': 0, 'E': 1}, 
        'A': {'B': 2, 'C': 2, 'D': 2, 'E': 0},
        'E': {'A': 2, 'B': 1, 'C': 1, 'D': 1}
    }
    G10 = {
        'A': {'B': 0, 'C': 0, 'D': 0, 'E': 1}, 
        'B': {'A': 2, 'C': 0, 'D': 1, 'E': 1}, 
        'C': {'A': 2, 'B': 2, 'D': 0, 'E': 2}, 
        'D': {'A': 2, 'B': 1, 'C': 2, 'E': 1}, 
        'E': {'A': 1, 'B': 1, 'C': 0, 'D': 1}
        }
    #score_type = 1
    score_type = 2

    #players = ['A', 'B', 'C']
    players = ['A', 'B', 'C', 'D', 'E']
    comes = ['win', 'tie', 'lose']

    if score_type == 1:
        points = [3, 1, 0]
        max_point = 3
    else:
        points = [2, 1, 0]
        max_point = 2
    
    match_list = list(itertools.combinations(players, 2))
    match_num = math.comb(len(players), 2)
    i = 0
    all_results = itertools.product(comes, repeat = match_num)
    #all_results = itertools.combinations_with_replacement(comes, match_num)
    for x in all_results:
        cjj = makeMatchGraph(match_list, x, score_type)
        if checkMatch(cjj):
            print(x)
            i += 1

    '''
    checkMatch(G8)
    checkMatch(G9)
    '''
    print(i)
    #checkMatch(G8)
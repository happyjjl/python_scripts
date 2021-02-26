# -*- coding: UTF-8 -*-
# 普林斯顿概率论读本第三章扑克牌问题：抽5张牌各种组合的概率验证
# 规则：1、扑克牌4种花色，每种花色1～13，没有大小王，共52张牌
#      2、Ace = 1, Jack = 11, Queen = 12, King = 13
#      3、Ace在顺子中，即可以作为1，也可以作为14，即[1,2,3,4,5]和[10,11,12,13,1]都是顺子
#      4、同花顺 > 铁支（四张相同的牌）> 葫芦（一对加三条）> 同花 > 顺子（不同花色）> 三条 > 两对 > 一对 > 5张啥都不是的牌
# 
# 本程序模拟n次，随机抽5张牌，统计每种组合出现的次数，得出概率

import random
import time

# 每种组合的理论概率
theory_probs = {
        'nothing':1302540 / 2598960,
        'one_pair':1098240 / 2598960,
        'two_pairs':123552 / 2598960,
        'three_of_a_kind':54912 / 2598960,
        'straight':10200 / 2598960,
        'flush':5108/ 2598960,
        'full_house':3744/2598960,
        'four_of_a_kind':624 / 2598960,
        'straight_flush':40 / 2598960}

# 判断是否为顺子，方法一
# 列表中最大值和最小值的差 = 4 ，需要考虑特殊情况 Ace
# 输入参数n: 必须是5个不同点数的列表，否则需要进行判断。后面调用此函数时上下文已经进行了判断，因此本函数内不做判断
def isStraight(n):
    if 1 in n and max(n) != 5:
            n.remove(1)
            n.append(14)        # 将1替换成14
    if max(n) - min(n) == 4:
        return True
    else:
        return False       

# 判断是否为顺子，方法二
# 列表排序后进行比较
# 输入参数n: 5个元素的列表
def isStraight2(n):
    straights = [[1, 2, 3, 4, 5],
                [2, 3, 4, 5, 6],
                [3, 4, 5, 6, 6],
                [4, 5, 6, 7, 8],
                [5, 6, 7, 8, 9],
                [6, 7, 8, 9, 10],
                [7, 8, 9, 10, 11],
                [8, 9, 10, 11, 12],
                [9, 10, 11, 12, 13],
                [1, 10, 11, 12, 13]]
    if sorted(n) in straights:
        return True
    else:
        return False 

# 判断是否为同花色，将花色列表转集合后根据集合长度是否为1进行判断
# 输入参数n：5个元素的列表
def isSameSuit(n):
    if len(set(n)) == 1:
        return True
    else:
        return False

# 统计5张牌点数的重复次数
# 输入是5张牌的列表，也可以用来统计字符串中各字母的重复次数
# 返回字典，键对应点数，值对应重复次数 
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

# 判断牌型
# 输入：五张牌的点数列表和对应的花色列表
# 返回：牌型对应的字符串
def getHands(points, suits):
    repeats = histogram(points)
    lenth_repeats = len(repeats)    
    if lenth_repeats == 5:         
        if isSameSuit(suits):
            if isStraight(points):
                return 'straight_flush'          # abcde（同花顺）
            else:
                return 'flush'                   # acefk (同花)
        else:
            if isStraight(points):
                return 'straight'                # abcde（非同花）
            else:
                return 'nothing'                 # 垃圾牌
    elif lenth_repeats == 4:
        return 'one_pair'                        # aabcd
    elif lenth_repeats == 3:
        if max(repeats.values()) == 2:
            return 'two_pairs'                   # aabbc
        else:
            return 'three_of_a_kind'             # aaabc
    else:
        if max(repeats.values()) == 4:
            return 'four_of_a_kind'              # aaaab
        else:
            return 'full_house'                  # aaabb


if __name__ == "__main__":
    num = int(input("请输入模拟的数: "))
    #if num < 1:
    #    print("请输入大于零的整数")
    #    quit()


    runners = [0] * 27
    runners[0] = 1
    runners[2] = 1
    runners[4] = 1
    runners[6] = 9
    runners[16] = 9
    runners[26] = 9
    #num = 9
    start = time.perf_counter()
    i = 1     # 循环计数器
    j = num
    k = 0
    bad_luck = 0
    while i < 26 and j > 2:
        if runners[i] == 0:
            runners[i] = j
        else:
            i += 1
            continue
        if i + j + 1 <= 26 and runners[i + j + 1] == 0:
            runners[i + j + 1] = j
        else:
            #bad_luck = 1
            runners[i] = 0
            j -= 1
            continue
        if i + j * 2 + 1 <= 26 and runners[i + j * 2 + 2] == 0:
            runners[i + j * 2 + 2] = j
        else:
            #bad_luck = 1
            runners[i] = 0
            runners[i + j + 1] = 0
            j -= 1
            continue
        #while j < 10:
        #    k = card[j]
        #    if card[j + k + 1] == k:
        #        print(card)
        #    j +=10
        i += 1
        j -= 1
    end = time.perf_counter()
    print(runners)
    print("Tests : {0} , Running time: {1} Seconds".format(0, end - start))
    #for key in hands:
    #    print("{0:15}\t{1:12}\tObserved Probability = {2:.8f}\tTheory Probability = {3:.8f}".format(key, hands[key], hands[key] / num, theory_probs[key]))
    
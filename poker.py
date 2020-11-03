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

num = 100000000                  # 模拟的总次数

# 每种组合的计数器
nothing = 0                     # 5张啥都不是的垃圾牌
onepair = 0                     # 一对
twopair = 0                     # 两对
threeofone = 0                  # 三条
straight = 0                    # 顺子
flush = 0                       # 同花
fullhouse = 0                   # 葫芦
fourofone = 0                   # 铁支
straightflush = 0               # 同花顺

# 用两维的嵌套列表表示52张牌，列表有52个元素，对应52张牌，每个元素是一个列表，列表有两个元素，第一个元素表示点数，第二个元素表示花色
deck52 = []
for x in range(1, 14):          # 初始化52张牌
    deck52.append([x, 1])       # 1 = 方块
    deck52.append([x, 2])       # 2 = 红桃
    deck52.append([x, 3])       # 3 = 黑桃
    deck52.append([x, 4])       # 4 = 梅花

# 判断是否为顺子，方法一
# 列表中最大值和最小值的差 = 4 ，需要考虑特殊情况 Ace
# 输入参数必须是5个不同点数的列表，否则需要进行判断。后面调用此函数时上下文已经进行了判断，因此本函数内不做判断
def isStraight(n):
    #if len(set(n)) != 5:
    #    return False
    if 1 in n and max(n) != 5:
            n.remove(1)
            n.append(14)        # 将1替换成14
    if max(n) - min(n) == 4:
        return True
    else:
        return False       

# 判断是否为顺子，方法二
# 列表排序后进行比较
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
def isSameSuit(n):
    if len(set(n)) == 1:
        return True
    else:
        return False

start = time.perf_counter()
i = 0     # 循环计数器
while i < num:
    card_point = []     # 牌的点数
    card_suit = []      # 牌的花色
    card = random.sample(deck52, 5)           # 从52张牌中无重复抽取5张，返回5个元素的列表    
    for x in card:
        card_point.append(x[0])
        card_suit.append(x[1])
    distinct_card = list(set(card_point))
    len_distinct_card = len(distinct_card)    # 将列表转换成集合，因为集合是无重复的，所以集合长度为5说明没有重复
    if len_distinct_card == 5:         
        if isSameSuit(card_suit):
            if isStraight(card_point):
                straightflush += 1            # abcde（同花顺）
            else:
                flush += 1                    # 同花
        else:
            if isStraight(card_point):
                straight += 1                 # abcde（非同花）
            else:
                nothing += 1
    else:
        if len_distinct_card == 4:
            onepair += 1                      # aabcd
        else:
            if len_distinct_card == 3:
                repeats = [0] * 3
                for k in range(0, 3):
                    repeats.append(card_point.count(distinct_card[k]))
                if max(repeats) == 2:
                    twopair += 1              # aabbc
                else:
                    threeofone += 1           # aaabc
            else:
                repeats = [0] * 2
                for k in range(0, 2):
                    repeats.append(card_point.count(distinct_card[k]))
                if max(repeats) == 4:
                    fourofone += 1            # aaaab
                else:
                    fullhouse += 1            # aaabb
    i += 1

end = time.perf_counter()

print("{0}次模拟中，垃圾牌的次数为{1}，Observed Probability = {2}，Theory Probability = {3}".format(num, nothing, nothing / num, 1302540 / 2598960))
print("{0}次模拟中，一对的次数为{1}，Observed Probability = {2}，Theory Probability = {3}".format(num, onepair, onepair / num, 1098240 / 2598960))
print("{0}次模拟中，两对的次数为{1}，Observed Probability = {2}，Theory Probability = {3}".format(num, twopair, twopair / num, 123552 / 2598960))
print("{0}次模拟中，三条的次数为{1}，Observed Probability = {2}，Theory Probability = {3}".format(num, threeofone, threeofone / num, 54912 / 2598960))
print("{0}次模拟中，顺子的次数为{1}，Observed Probability = {2}，Theory Probability = {3}".format(num, straight, straight / num, 10200 / 2598960))
print("{0}次模拟中，同花的次数为{1}，Observed Probability = {2}，Theory Probability = {3}".format(num, flush, flush / num, 5108/ 2598960))
print("{0}次模拟中，葫芦的次数为{1}，Observed Probability = {2}，Theory Probability = {3}".format(num, fullhouse, fullhouse / num, 3744/2598960))
print("{0}次模拟中，铁支的次数为{1}，Observed Probability = {2}，Theory Probability = {3}".format(num, fourofone, fourofone / num, 624 / 2598960))
print("{0}次模拟中，同花顺的次数为{1}，Observed Probability = {2}，Theory Probability = {3}".format(num, straightflush, straightflush / num, 40 / 2598960))

#print(nothing + onepair + twopair + threeofone + straight + flush + fullhouse + fourofone + straightflush)
print('Running time: %s Seconds'%(end-start))
# -*- coding: UTF-8 -*-
# 普林斯顿概率论读本第三章扑克牌问题：抽5张牌都不相同的概率验证
# 扑克牌4种花色，将方块看作1～13，将其它三种花色看作14～52，如果随机数在1和13之间，则认为抽中方块
# 玩1000000次，统计每个人的胜利次数，得出概率
import random

num = 10000000                  # 实验的总次数

nothing = 0                     # 5张啥都不是的牌
onepair = 0                     # 一对
twopair = 0                     # 两对
threeofone = 0                  # 三条
straight = 0                    # 顺子
flush = 0                       # 同花
fullhouse = 0                   # 葫芦
fourofone = 0                   # 铁支
straightflush = 0               # 同花顺
deck52 = []
for x in range(1, 14):          # 初始化52张牌
    deck52.append([x, 1])       # 方块
    deck52.append([x, 2])       # 红桃
    deck52.append([x, 3])       # 黑桃
    deck52.append([x, 4])       # 梅花


def isStraight(n):
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

def isSameType(n):
    if len(set(n)) == 1:
        return True
    else:
        return False


i = 0
while i < num:
    card_number = []
    card_type = []
    card = random.sample(deck52, 5)           # 从52张牌中无重复抽取5张，返回5个元素的列表    
    for x in card:
        card_number.append(x[0])
        card_type.append(x[1])
    distinct_card = list(set(card_number))
    len_distinct_card = len(distinct_card)    # 将列表转换成集合，因为集合是无重复的，所以集合长度为5说明没有重复
    if len_distinct_card == 5:         
        if isSameType(card_type):
            if isStraight(card_number):
                straightflush += 1
            else:
                flush += 1
        else:
            if isStraight(card_number):
                straight += 1
            else:
                nothing += 1
    else:
        if len_distinct_card == 4:
            onepair += 1                      # aabcd
        else:
            if len_distinct_card == 3:
                pairs = [0] * 3
                for k in range(0, 3):
                    pairs.append(card_number.count(distinct_card[k]))
                if max(pairs) == 2:
                    twopair += 1              # aabbc
                else:
                    threeofone += 1           # aaabc
            else:
                pairs = [0] * 2
                for k in range(0, 2):
                    pairs.append(card_number.count(distinct_card[k]))
                if max(pairs) == 4:
                    fourofone += 1            # aaaab
                else:
                    fullhouse += 1            # aaabb
    i += 1

print("{0}次实验中，啥都不是的次数为{1}，Observed Probability = {2}，Theory Probability = {3}".format(num, nothing, nothing / num, 2112 / 4165))
print("{0}次实验中，一对的次数为{1}，Observed Probability = {2}，Theory Probability = {3}".format(num, onepair, onepair / num, 352 / 833))
print("{0}次实验中，两对的次数为{1}，Observed Probability = {2}，Theory Probability = {3}".format(num, twopair, twopair / num, 123552 / 2598960))
print("{0}次实验中，三条的次数为{1}，Observed Probability = {2}，Theory Probability = {3}".format(num, threeofone, threeofone / num, 54912 / 2598960))
print("{0}次实验中，顺子的次数为{1}，Observed Probability = {2}，Theory Probability = {3}".format(num, straight, straight / num, 128 / 32487))
print("{0}次实验中，同花的次数为{1}，Observed Probability = {2}，Theory Probability = {3}".format(num, flush, flush / num, 5108/ 2598960))
print("{0}次实验中，葫芦的次数为{1}，Observed Probability = {2}，Theory Probability = {3}".format(num, fullhouse, fullhouse / num, 3744/2598960))
print("{0}次实验中，铁支的次数为{1}，Observed Probability = {2}，Theory Probability = {3}".format(num, fourofone, fourofone / num, 624 / 2598960))
print("{0}次实验中，同花顺的次数为{1}，Observed Probability = {2}，Theory Probability = {3}".format(num, straightflush, straightflush / num, 40 / 2598960))

print(nothing + onepair + twopair + threeofone + straight + flush + fullhouse + fourofone + straightflush)

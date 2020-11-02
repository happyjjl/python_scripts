# -*- coding: UTF-8 -*-
# 普林斯顿概率论读本第三章扑克牌问题：抽5张牌都不相同的概率验证
# 扑克牌4种花色，将方块看作1～13，将其它三种花色看作14～52，如果随机数在1和13之间，则认为抽中方块
# 玩1000000次，统计每个人的胜利次数，得出概率
import random

num = 1000000                 # 实验的总次数
deck = list(range(1, 14)) * 4   # 初始化52张牌
distinct = 0                    # 5张牌都不同的次数
onepair = 0                     # 一对
twopair = 0                     # 两对
threeofone = 0                  # 三条

i = 0
while i < num:
    '''
    a = deck[random.randint(0, 51)]
    b = deck[random.randint(0, 51)]
    c = deck[random.randint(0, 51)]
    d = deck[random.randint(0, 51)]
    e = deck[random.randint(0, 51)]
    card = [a, b, c, d, e]
    '''
    card = random.sample(deck, 5) # 从52张牌中无重复抽取5张，返回5个元素的列表
    distinct_card = list(set(card))
    len_distinct_card = len(distinct_card)
    if len_distinct_card == 5:       # 将列表转换成集合，因为集合是无重复的，所以集合长度为5说明没有重复  
        distinct += 1
    if len_distinct_card == 4:
        onepair += 1
    if len_distinct_card == 3:
        pairs = [0] * 3
        for k in range(0, 3):
            pairs.append(card.count(distinct_card[k]))
        if max(pairs) == 2:
            twopair += 1
        else:
            threeofone += 1
        
    i += 1

print("{0}次实验中，5张牌都不同的次数为{1}，Probability = {2}".format(num, distinct, distinct / num))
print("{0}次实验中，一对的次数为{1}，Probability = {2}".format(num, onepair, onepair / num))
print("{0}次实验中，两对的次数为{1}，Probability = {2}".format(num, twopair, twopair / num))
print("{0}次实验中，三条的次数为{1}，Probability = {2}".format(num, threeofone, threeofone / num))



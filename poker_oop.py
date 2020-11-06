# -*- coding: UTF-8 -*-
# 普林斯顿概率论读本第三章扑克牌问题：抽5张牌各种组合的概率验证
# 规则：1、扑克牌4种花色，每种花色1～13，没有大小王，共52张牌
#      2、Ace = 1, Jack = 11, Queen = 12, King = 13
#      3、Ace在顺子中，即可以作为1，也可以作为14，即[1,2,3,4,5]和[10,11,12,13,1]都是顺子
#      4、同花顺 > 铁支（四张相同的牌）> 葫芦（一对加三条）> 同花 > 顺子（不同花色）> 三条 > 两对 > 一对 > 5张啥都不是的牌
# 
# 本程序模拟n次，随机抽5张牌，统计每种组合出现的次数，得出概率
# 此版本为oop改写，定义了三种类：单张牌、一副牌、一副手牌，期中一副手牌继承自一副牌，效率降低

import random
import time
from collections import Counter

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

class Card:
    '''
    一张牌，属性为rank和suit
    rank:
        2~10
        Ace     --> 1
        Jack    --> 11
        Queen   --> 12
        King    --> 13
    suit:
        Spades   --> 3
        Hearts   --> 2
        Diamonds --> 1
        Clubs    --> 0
    '''
    
    # 用列表下标进行rank和suit的映射
    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, "Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]

    def __init__(self, suit = 0, rank = 2):
        if suit < 0 or suit > 3:
            print("wrong suit, please input integer between 0 and 3!")
            return
        if rank < 0 or rank > 13:
            print("wrong rank, please input integer between 0 and 13!")
            return
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "{0} of {1}".format(Card.rank_names[self.rank], Card.suit_names[self.suit])

class Deck:
    '''
    定义一副牌，共有52张
    '''
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        print_str = []
        for card in self.cards:
            print_str.append(str(card))
        return "\n".join(print_str)

    # 洗牌
    def shuffle(self):
        random.shuffle(self.cards)

    # 随机抽取n张牌，默认为5张
    def choice(self, n = 5):
        return random.sample(self.cards, n)

    # 添加牌
    def add_cards(self, cards):
        for card in cards:
            self.cards.append(card)

class Hand(Deck):
    '''定义一手牌，默认0张'''
    def __init__(self):
        self.cards = []
        self.type = []

    # 判断手牌的类型
    def getType(self):
        if len(self.cards) == 0 or len(self.type) == 1:
            return self.type
        points = []
        suits = []
        for card in self.cards:
            points.append(card.rank)
            suits.append(card.suit)
        repeats = Counter(points)
        lenth_repeats = len(repeats)    
        if lenth_repeats == 5:         
            if isSameSuit(suits):
                if isStraight(points):
                    self.type = 'straight_flush'          # abcde（同花顺）
                else:
                    self.type = 'flush'                   # acefk (同花)
            else:
                if isStraight(points):
                    self.type = 'straight'                # abcde（非同花）
                else:
                    self.type = 'nothing'                 # 垃圾牌
        elif lenth_repeats == 4:
            self.type = 'one_pair'                        # aabcd
        elif lenth_repeats == 3:
            if max(repeats.values()) == 2:
                self.type = 'two_pairs'                   # aabbc
            else:
                self.type = 'three_of_a_kind'             # aaabc
        else:
            if max(repeats.values()) == 4:
                self.type = 'four_of_a_kind'              # aaaab
            else:
                self.type = 'full_house'                  # aaabb
        return self.type

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


if __name__ == "__main__":

    num = int(input("请输入模拟的次数: "))
    if num < 1:
        print("请输入大于零的整数")
        quit()

    # 每种组合的计数器
    hand_types = {
        'nothing':0,                     # 5张啥都不是的垃圾牌
        'one_pair':0,                    # 一对
        'two_pairs':0,                   # 两对
        'three_of_a_kind':0,             # 三条
        'straight':0,                    # 顺子
        'flush':0,                       # 同花
        'full_house':0,                  # 葫芦
        'four_of_a_kind':0,              # 铁支
        'straight_flush':0}              # 同花顺

    deck52 = Deck()                      # 初始化一副牌

    start = time.perf_counter()
    i = 0     # 循环计数器
    while i < num:
        hand = Hand()                    # 初始化手牌，手里是空的
        hand_five = deck52.choice()      # 从52张牌中无重复抽取5张
        hand.add_cards(hand_five)        # 将抽取的牌放到手中
        hand_types[hand.getType()] += 1  # 返回手牌的类型并计数
        i += 1
    end = time.perf_counter()
    print("Tests : {0} , Running time: {1:.2f} Seconds".format(num, end - start))
    for key in hand_types:
        print("{0:15}\t{1:12}\tObserved Probability = {2:.8f}\tTheory Probability = {3:.8f}".format(key, hand_types[key], hand_types[key] / num, theory_probs[key]))
    
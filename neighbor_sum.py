# -*- coding: UTF-8 -*-
# 美国大联盟2020-2021第20题
# 
# 

import itertools
import random

# allLengthCombinationSum(list)
# 功能：返回列表中所有的任意元素的和
# 输入：列表，列表为正整数
# 输出：列表中任意元素的和形成的集合
#       集合包括:
#           单个元素
#           所有两个元素的和
#           所有三个元素的和
#           。。。
#           。。。
#           所有n-1个元素的和（n为输入列表的长度）
def allLengthCombinationSum(mylist):
    n = len(mylist)
    newlist = []
    sumlist = []
    for i in range(1, n + 1):
        newlist += list(itertools.combinations(mylist, i))
    for x in newlist:
        sumlist.append(sum(x))
    return set(sumlist)
    

if __name__ == "__main__":
    num = int(input("请输入模拟的次数: "))
    #numbers = range(1,100)
    neighbor_sums = [26, 8, 19, 13, 17, 10, 4, 19, 24]
    bingo = 0
    k = 0
    while k < num:
        ten_numbers = random.sample(numbers, 10) # 从1-99中任意选择10个数字
        for i in range(1, 6):  # 1 vs 9，2 vs 8，3 vs 7，4 vs 6，5 vs 5
            found = 0
            left_number = list(itertools.combinations(ten_numbers, i))
            for x in left_number:
                left_set = set(x)                                   # 两个集合中的第一个
                right_set = set(ten_numbers).difference(left_set)   # 两个集合的另一个
                left_sums = allLengthCombinationSum(left_set)       # 计算集合中所有可能的和
                right_sums = allLengthCombinationSum(right_set)     # 计算集合中所有可能的和
                if not left_sums.isdisjoint(right_sums):            # 找到一个相等的和即可
                    print(left_set, right_set, left_sums.intersection(right_sums))
                    found = 1
                    bingo += 1
                    break
            if found:break
        k += 1
    print('模拟次数：', num)
    print('满足次数：', bingo)
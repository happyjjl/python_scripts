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
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    neighbor_sums = [26, 8, 19, 13, 17, 10, 4, 19, 24]
    p = itertools.permutations(numbers)
    #bingo = 0
    m = 0
    for x in p:
        m += 1
        k = 0
        if x[2] + x[3] in neighbor_sums:
            k += 1
        else:
            continue
        if x[0] + x[1] + x[4] in neighbor_sums:
            k += 1
        else:
            continue
        if x[1] + x[2] + x[5] + x[6] + x[8] in neighbor_sums:
            k += 1
        else:
            continue
        if x[2] + x[5] + x[7] in neighbor_sums:
            k += 1
        else:
            continue
        if x[3] + x[4] + x[8] in neighbor_sums:
            k += 1
        else:
            continue
        if x[3] + x[8] in neighbor_sums:
            k += 1
        else:
            continue
        if x[4] + x[8] in neighbor_sums:
            k += 1
        else:
            continue
        if x[3] + x[5] + x[6] + x[7] in neighbor_sums:
            k += 1
        else:
            continue
        #m += 1
        if k == 8:
            print(x)
            print('运行次数：', m)
            break
    
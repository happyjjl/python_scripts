# -*- coding: UTF-8 -*-
# 美国大联盟2020-2021第20题
# 
# 

import itertools
import random

# 
#      A        B              S(A) = C
#       \     /   \            S(B) = C + D
#        \   /     \           S(C) = A + B + D + E
#         C ------- D          S(D) = B + C + F + G + I
#        /        / | \        S(E) = C + F + H
#       /        /  |  \       S(F) = D + E + I
#      E ------ F ----- G      S(G) = D + I
#       \        \  |  /       S(H) = E + I
#        \        \ | /        S(I) = D + F + G + H
#         H ------- I
# 算法： 
#    将1-9的不同排列对应到ABCDEFGHI
#    按照上图，从S(B)开始计算对应的和，每次计算后，判断和是否在题目给出的9个和里面
#    如果连续8次计算的和都在题目给出的9个和里面，则此时的排列即符合题意的解
#

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    neighbor_sums = [26, 8, 19, 13, 17, 10, 4, 19, 24]
    p = itertools.permutations(numbers)
    m = 0
    for x in p:
        m += 1
        k = 0
        if x[2] + x[3] in neighbor_sums:
            k += 1
        else:
            continue
        if x[0] + x[1] + x[3] + x[4] in neighbor_sums:
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
        if k == 8:
            print(x)
            print('运行次数：', m)
            break
    
# -*- coding: UTF-8 -*- 
#
#  a b c d 四个区域，用四种不同的颜色染色，相邻不能同色的方法有几种？
#         | 
#       a | b
#     —————————
#       d | c
#         |
#
import itertools

cjj = itertools.product('abcd', repeat=4)
i = 0
for x in cjj:
    if x[0] != x[1] and x[1] != x[2] and x[2] != x[3] and x[3] != x[0]:
        print(x)
        i += 1
print(i)
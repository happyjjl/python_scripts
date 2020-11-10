# -*- coding: UTF-8 -*-
# 普林斯顿概率论读本第六章6字符车牌4字符相同概率：6.1.2
#

import random
import math
import time


uppercase_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'G', 'K', 'L', 'M', 
                  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digi_char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

if __name__ == "__main__":

    test = int(input("请输入模拟实验的次数: "))
    if test < 1:
        print("请输入大于零的整数")
        quit()

    found = 0       # 4位字符相同次数
    i = 0           # 循环次数
    start = time.perf_counter()
    while i < test:
        
        num_sames = 0

        for k in range(3):
            x = random.choice(uppercase_char)
            y = random.choice(uppercase_char)
            if x == y:
                num_sames += 1
            u = random.choice(digi_char)
            v = random.choice(digi_char)
            if u == v:
                num_sames += 1
        
        if num_sames == 4:
            found += 1
            
        i += 1

    print("found! :", found)
    end = time.perf_counter()
    print("Running time: {0:.2f} Seconds".format(end - start))
    print("Theoy Probablity\t= {0:.6f}".format(72817368000 / (26**6 * 10**6)))
    print("Observed Probability\t= {0:.6f}".format(found / test))

# -*- coding: UTF-8 -*-
# 普林斯顿概率论读本第五章错排问题：5.3.3
#

import random
import math
import time

if __name__ == "__main__":

    num = int(input("请输入排列对象的个数: "))
    test = int(input("请输入模拟实验的次数: "))
    if num < 1 or test < 1:
        print("请输入大于零的整数")
        quit()
        
    # 根据公式计算错排的理论概率
    theoy_prob = 0
    for x in range(num + 1):
        theoy_prob += (-1)**x / math.factorial(x) 

    objects = list(range(num))
    found = 0       # 错排次数
    i = 0           # 循环次数
    start = time.perf_counter()
    while i < test:
        k = 0       # 不在初始位置的次数
        arrange = random.sample(objects, num)
        for x in range(num):
            if arrange[x] == x:
                break
            else:
                k += 1
        if k == num:
            found += 1
        i += 1
    end = time.perf_counter()
    print("Running time: {0:.2f} Seconds".format(end - start))
    print("Theoy Probablity\t= {0:.6f}".format(theoy_prob))
    print("Limit           \t= {0:.6f}".format(1 / math.e))
    print("Observed Probability\t= {0:.6f}".format(found / test))

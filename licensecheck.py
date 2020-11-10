# -*- coding: UTF-8 -*-
# 普林斯顿概率论读本第六章6字符车牌4字符相同概率：6.1.2
#

import random
import math
import time

def getSameKinds(lista,listb):
    #a = lista
    numagree = 0
    for x in listb:
        if x in lista:
            numagree += 1
            lista.remove(x)
    return numagree

uppercase_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'G', 'K', 'L', 'M', 
                  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digi_char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

if __name__ == "__main__":

    #num = int(input("请输入排列对象的个数: "))
    test = int(input("请输入模拟实验的次数: "))
    if test < 1:
        print("请输入大于零的整数")
        quit()

    
    # 根据公式计算错排的理论概率
    

    #objects = list(range(num))
    found = 0       # 错排次数
    i = 0           # 循环次数
    start = time.perf_counter()
    while i < test:
        license_a = random.choices(uppercase_char, k = 3) + random.choices(digi_char, k = 3) 
        license_b = random.choices(uppercase_char, k = 3) + random.choices(digi_char, k = 3)
        
        '''
        license_a = []
        license_b = []
        for k in range(3):
            x = random.choice(uppercase_char)
            y = random.choice(uppercase_char)
            if x == y:

            license_a.append(random.choice(uppercase_char))
            license_a.append(random.choice(digi_char))
            license_b.append(random.choice(uppercase_char))
            license_b.append(random.choice(digi_char))
        
        '''
        #cjj = license_a
        num_sames = 0
        for k in range(6):
            if license_a[k] == license_b[k]:
                num_sames += 1
        #num_sames = getSameKinds(license_a, license_b)
        if num_sames == 4:
            found += 1
            #print(cjj)
            #print(license_b) 
            #print("--------------")
        i += 1
    print("found! :", found)
    end = time.perf_counter()
    print("Running time: {0:.2f} Seconds".format(end - start))
    print("Theoy Probablity\t= {0:.6f}".format(72817368000 / (26**6 * 10**6)))
    #print("Limit           \t= {0:.6f}".format(1 / math.e))
    print("Observed Probability\t= {0:.6f}".format(found / test))

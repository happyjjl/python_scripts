# -*- coding: UTF-8 -*-
# 美国大联盟2020-2021第22题
# 
# 

import itertools

def isSelfDescriptiveNumber(n):
	s = str(n)
	return all(s.count(str(i)) == int(ch) for i, ch in enumerate(s))
# 判断是否为顺子，方法一
# 列表中最大值和最小值的差 = 4 ，需要考虑特殊情况 Ace
# 输入参数n: 必须是5个不同点数的列表，否则需要进行判断。后面调用此函数时上下文已经进行了判断，因此本函数内不做判断


if __name__ == "__main__":
    #num = int(input("请输入上限值: "))
    all_number = list(set(list(itertools.permutations([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]))))
    #all_number = list(itertools.permutations([1, 1, 2, 2, 3]))
    #all_number = list(itertools.permutations([1, 1, 2, 2, 2, 3, 3, 3, 5, 5]))
    for x in all_number:
        found = 0
        #for i in [1, 2, 3, 4, 5, 6, 7, 8]:
        #for i in [1, 2, 3]:
        for i in [1, 2, 3, 4, 5, 6, 7, 8]:
            if x[i - 1] + x[i + 1] == x[i] or abs(x[i - 1] - x[i + 1]) == x[i]:
                found += 1
            else:
                break
        #if found == 8:
        if found == 8:
            print(x)
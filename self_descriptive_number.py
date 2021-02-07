# -*- coding: UTF-8 -*-
# 美国大联盟2020-2021第23题
# 
# https://medium.com/@divyangrpatel/self-descriptive-number-best-algorithm-95b281e6de05
# https://rosettacode.org/wiki/Self-describing_numbers#Python



def isSelfDescriptiveNumber(n):
	s = str(n)
	return all(s.count(str(i)) == int(ch) for i, ch in enumerate(s))
# 判断是否为顺子，方法一
# 列表中最大值和最小值的差 = 4 ，需要考虑特殊情况 Ace
# 输入参数n: 必须是5个不同点数的列表，否则需要进行判断。后面调用此函数时上下文已经进行了判断，因此本函数内不做判断


if __name__ == "__main__":
    num = int(input("请输入上限值: "))

    for i in range(num):
        if (isSelfDescriptiveNumber(i)):
            print(i)
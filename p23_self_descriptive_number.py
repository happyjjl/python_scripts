# -*- coding: UTF-8 -*-
# 美国大联盟2020-2021第23题
# 
# https://medium.com/@divyangrpatel/self-descriptive-number-best-algorithm-95b281e6de05
# https://rosettacode.org/wiki/Self-describing_numbers#Python



def isSelfDescriptiveNumber(n):
	s = str(n)
	return all(s.count(str(i)) == int(ch) for i, ch in enumerate(s))

if __name__ == "__main__":
    num = int(input("请输入上限值: "))

    for i in range(num):
        if (isSelfDescriptiveNumber(i)):
            print(i)
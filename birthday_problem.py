# -*- coding: UTF-8 -*-
# 普林斯都概率论读本第一章生日问题

# 利用递归，计算n个人的至少两个人生日相同的概率
def getShare(n):
    if n == 1:
        return n
    else:
        return getShare(n - 1) * (365 - (n - 1)) / 365

if __name__ == "__main__":

    number = int(input("请输入教室的人数: "))
    '''
    if number <= 0:
        print("请输入大于零的整数，谢谢!")
    else:
        print("教室人数为", number, "时，至少两个人生日相同的概率为:", 1 - getShare(number))
    '''

    if number <= 0:
        print("请输入大于零的整数，谢谢!")
    else:
        print("教室人数从 1 到", number, "时，至少两个人生日相同的概率为:")
        for i in range(1, number + 1):
            print("n =", i, ": probability =", 1 - getShare(i))
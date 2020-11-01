# -*- coding: UTF-8 -*-
# 普林斯都概率论读本第二章将正整数数写成4个整数平方和
# n = a * a + b * b + c * c + d * d
# d <= c <= b <= a
import math

def sumFourSquares(n):
    #count = 0
    sum_found = []
    for a in range(0, int(math.sqrt(n)) + 1):
        for b in range(0, a + 1):
            for c in range(0, b + 1):
                for d in range(0, c + 1):
                    if a * a + b * b + c * c + d * d == n:
                        #count += 1
                        sum_found.append([d, c, b, a])
    #print(count)
    return sum_found

if __name__ == "__main__":

    number = int(input("请输入一个正整数:"))
    if number <= 0:
        print("请输入大于零的整数，谢谢")
    else:
        my_sums = sumFourSquares(number)
        print("{0}写成四个数的平方和的方法有{1}种:".format(number, len(my_sums)))
        print(*my_sums, sep = "\n")
        print("--------------------")
        print(my_sums)
        print("--------------------")
        for x in my_sums: print(x)




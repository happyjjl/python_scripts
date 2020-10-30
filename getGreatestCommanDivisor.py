# -*- coding: UTF-8 -*-
# greatest common divisor      
# least common multiple
# 最大公约数和最小公倍数
# gcd and lcm
# 
from getFactor import getAllFactors
import getFactor

def getGreatestCommonDivisor(x, y):
    #set1 = set(getAllFactors(x))
    #set2 = set(getAllFactors(y))
    return max(set(getAllFactors(x)).intersection(set(getAllFactors(y))))  # 将列表转换成集合后求交集，然后取最大值

def getGreatestCommonDivisor2(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if x % i == 0 and y % i == 0:
            common_divisor = i
    return common_divisor

def getLeastCommonMultiple(x, y):
    step_x = x
    step_y = y
    while x != y:
        if x > y:
            y += step_y
        else:
            x += step_x
    return x

if __name__ == "__main__":

    number1 = int(input("请输入第一个正整数: "))
    number2 = int(input("请输入第二个正整数: "))
    '''
    greatest_common_divisor = getGreatestCommonDivisor2(number1, number2)
    print("Greatest Common Divisor of", number1, number2, ":")
    print(greatest_common_divisor)
    '''
    print("Least Common Multiple of", number1, "and", number2, ":", getLeastCommonMultiple(number1, number2))
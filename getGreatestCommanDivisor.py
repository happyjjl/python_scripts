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

# 欧几里得辗转相除法：
# 求两个数a和b的最大公约数(a,b)，可以用如下的定理：
#   a = b * q + r   其中q为倍数，r为余数
#   (a,b) = (b,r)
def get_gcd(x, y):
    while y != 0:
        temp = y
        y = x % y
        x = temp
    return x

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
 
    print("Greatest Common Divisor of", number1, "and", number2, ":", get_gcd(number1, number2))
    print("Least Common Multiple of", number1, "and", number2, ":", getLeastCommonMultiple(number1, number2))
# -*- coding: UTF-8 -*-
 
# 求从1到某个数之间因子数量等于某个数的数量，例如：1到100的自然数中，恰好有6个因子的数有几个？
# 


# 很好的方法
def getPrimeFactor2(n):
    factors = []
    divisor = 2 
    while n >= divisor:
        if( n % divisor == 0):
            factors.append(divisor)
            n = n / divisor  #更新
        else:
            divisor += 1  #同时更新除数值，不必每次都从头开始
    return factors

# 分解所有因数
def getAllFactors(n):
    factors = []
    divisor = 1
    while n >= 2 * divisor:
        if n % divisor ==0:
            factors.append(divisor)
        divisor += 1
    factors.append(n)
    return factors

if __name__ == "__main__":

    number = int(input("请输入范围上限: "))
    factor_num = int(input("请输入因子个数: "))
    #factors = getPrimeFactor2(number)
    #print("Prime Factors:")
    #if len(factors) == 1:
    #    print(number, " = ", "1*", factors[0], sep = "")
    #else:
    #    print(number, "=", "*".join(str(i) for i in factors))
    factor_found = []
    found = 0
    i = 1
    while i <= number:
        factor_found = getAllFactors(i)
        if(len(factor_found)) == factor_num:
            found += 1
            print(i, ":", factor_found)
        i += 1

    print("恰好有", factor_num, "个因子的数的数量为:", found)
    #print(found)
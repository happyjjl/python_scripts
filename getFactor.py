# -*- coding: UTF-8 -*-
 
# 分解因数和质因数
# 

# 有重复语句，不够优雅 
def getPrimeFactor(n):
    factors = []
    quotient = 0
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            quotient = n / i
            if quotient == 1:
                break
            else:
                n = quotient
        if quotient == 1:
            break
        else:
            i += 1
    return factors

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

    number = int(input("请输入想要分解质因数的正整数: "))
    factors = getPrimeFactor2(number)
    print("Prime Factors:")
    if len(factors) == 1:
        print(number, " = ", "1*", factors[0], sep = "")
    else:
        print(number, "=", "*".join(str(i) for i in factors))

    
    print("All Factors:")
    print(getAllFactors(number))
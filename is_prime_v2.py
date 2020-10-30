# -*- coding: utf-8 -*-
# import math
# method of find prime
# https://www.jianshu.com/p/da3161905f28
# https://www.pythonf.cn/read/152396
# https://skywt.cn/posts/aishi-eular-shai
# https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n   各种算法性能比较
import time

#my_number = int(input())
n = 10
# get prime 
def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:     # 循环到n的平方根，原因：一个合数 n = a * b，则ab中必有一个小于或等于n的平方根。可以用反证法证明：
        if n % i == 0:    # 假设ab都大于n的平方根，则 a * b > n，与 a * b = n矛盾
            return False
        else:
            i = i + 2     # only odds number divided
    return True

# find all primes before N
# method 1: regular
def getPrimes(n):
    i = 1
    primes = []
    while i <= n:
        if (isPrime(i)):
            primes.append(i)
        i = i + 1
    return primes

# method 2: sieve by Eratosthenes
# 埃拉托斯特尼筛法：
# 给出要筛数值的范围n，用n的平方根以内的质数，先后划掉这些质数的倍数，最后剩下的就是要找的所有质数。
# 先用2去筛，即把2留下，把2的倍数剔除掉；再用下一个素数，也就是3筛，把3留下，把3的倍数剔除掉；接下
# 去用下一个素数5筛，把5留下，把5的倍数剔除掉；不断重复下去
# https://zh.wikipedia.org/wiki/%E5%9F%83%E6%8B%89%E6%89%98%E6%96%AF%E7%89%B9%E5%B0%BC%E7%AD%9B%E6%B3%95
def getPrimesByEratosthenes(n):
    sieve = [True] * (n + 1)                        # 将数列0，1，2，3...n对应的列表值都设为True，开始时整个数列都认为是质数
    for i in range(2, int(n ** 0.5) + 1):           # 循环到n的平方根而不是n，时因为当 i > n的平方根后，下面的循环 j 会从 i 的平方开始，已经超过 n 了
        if sieve[i]:
            for j in range(i * i, n + 1, i):        # 从 i * i 开始循环而不是从 i * 2 开始，这是因为 i * 2 到 i * i 之间的倍数已经在前面筛过了，比如当
                                                    # i = 7 时，倍数2，3，5分别在 i = 2 、i = 3 和 i = 5 时筛过了，4和6偶数倍在 i = 2 时也筛过了
                sieve[j] = False                    # 从2开始，依次将每个质数的倍数筛掉，即将每个质数的倍数对应的列表值改为False
    return[prime for prime in range(2, n +1) if sieve[prime]]   # 返回列表值为True对应的数列值（即找到的质数）

# method 3: sieve by Eular
# https://blog.csdn.net/qq_39763472/article/details/82428602
# https://blog.csdn.net/artistkeepmonkey/article/details/83688629
# https://my.oschina.net/gschen/blog/4618629
def getPrimesByEular(n):
    sieve = [True] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if sieve[i]:
            primes.append(i)
        for prime in primes:
            if i * prime > n:
                break
            sieve[i * prime] = False
            if i % prime == 0:
                break
    return primes
    
# 欧拉筛是埃氏筛的运行时间的2倍，奇怪
if __name__ == "__main__":
    #N = 100000000
    N = 2000000

    #print("Get primes:", "N =", N)
    #start = time.perf_counter()
    #primes = getPrimes(N) 
    #end = time.perf_counter()
    #print('Running time: %s Seconds'%(end-start))

    #print(primes)
    #print("total", len(primes), "primes!")

    print("Get primes by Eratosthenes:", "N =", N)
    start = time.perf_counter()
    primes = getPrimesByEratosthenes(N) 
    end = time.perf_counter()
    print('Running time: %s Seconds'%(end-start))

    #print(primes)
    print("total", len(primes), "primes!")    

    print("Get primes by Eular:", "N =", N)
    start = time.perf_counter()
    primes = getPrimesByEular(N)   
    end = time.perf_counter()
    print('Running time: %s Seconds'%(end-start))

    #print(primes)
    print("total", len(primes), "primes!")     

    #if isPrime(961):
    #    print("yes!")
    #else:
    #    print("NO!")                 

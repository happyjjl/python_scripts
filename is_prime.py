# -*- coding: utf-8 -*-
#import math
# method of find prime
# https://www.jianshu.com/p/da3161905f28
# https://www.pythonf.cn/read/152396
# https://skywt.cn/posts/aishi-eular-shai
# https://zh.wikipedia.org/wiki/%E5%9F%83%E6%8B%89%E6%89%98%E6%96%AF%E7%89%B9%E5%B0%BC%E7%AD%9B%E6%B3%95

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
    while i * i <= n:     # loop to square root of n,  a * b = n, if a > square root of n, then b will repeat a
        if n % i == 0:
            return False
        else:
            i = i + 2     # only odds number divided
    return True

# find all primes before N
# method 1: regular
def getPrimes(n):
    i = 1
    count = 0
    while i <= n:
        if (isPrime(i)):
            print(i)
            count = count + 1
        i = i + 1
    print("total", count, "primes!")

# method 2: sieve by Eratosthenes
def getPrimesByEratosthenes(n):
    sieve = [True] * (n + 1)
    count = 0
    for i in range(2, n + 1):
        if sieve[i]:
            print(i)
            count = count + 1
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    print("total", count, "primes!")

def getPrimesByEratosthenes2(n):
    sieve = [True] * (n + 1)
    count = 0
    for i in range(2, int(n ** 0.5)):
        if sieve[i]:
            #print(i)
            #count = count + 1
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    #for i in range(2, n + 1):
    #    if sieve[i]:
    #        print(i)
    #        count = count + 1
    #print("total", count, "primes!")
    return[x for x in range(2, n +1) if sieve[x]]
    
# method 3: sieve by Eular
#def getPrimesByEular(n):
    

start = time.perf_counter()
#getPrimes(1000000)
end = time.perf_counter()
print('Running time: %s Seconds'%(end-start))

#getPrimesByEratosthenes2(101)

if __name__ == "__main__":
    primes = getPrimesByEratosthenes2(101)
    print(primes)
    print("total", len(primes), "primes!")    
#if isPrime(my_number):
#    print("prime found!")
#else:
#    print("not prime!")
                    

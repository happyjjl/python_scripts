# -*- coding: UTF-8 -*-
# 递归的用法
def getFibonacci(n):
    if n <= 1:
        return n
    else:
        return getFibonacci(n - 1) + getFibonacci(n - 2)

if __name__ == "__main__":

    number = int(input("请输入斐波那契数列的项目: "))
    if number <= 0:
        print("请输入大于零的整数，谢谢")
    else:
        print("前", number, "项的斐波那契数列为:")
        for i in range(number):
            print(getFibonacci(i))

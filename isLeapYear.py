# -*- coding: UTF-8 -*-
 
# Filename : test.py
# author by : www.runoob.com
 
def isLeap(year):
    if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0 :  # 非整百年能被4整除的为闰年
        return True   
    else:
        return False



if __name__ == "__main__":
    year = int(input("输入一个年份: "))
    if isLeap(year):
        print("{0} 是闰年".format(year))       
    else:
        print("{0} 不是闰年".format(year))
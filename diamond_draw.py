# -*- coding: UTF-8 -*-
# 普林斯都概率论读本第一章扑克牌抽方块问题的概率验证
# 扑克牌4种花色，将方块看作1～13，将其它三种花色看作14～52，如果随机数在1和13之间，则认为抽中方块
# 玩1000000次，统计每个人的胜利次数，得出概率
import random
awin = 0   # Alice
bwin = 0   # Bob
cwin = 0   # Charlie
num = 1000000

while awin + bwin + cwin < num:
    if random.randint(1, 52) <= 13:
        awin += 1
    else:
        if random.randint(1, 52) <= 13:
            bwin += 1
        else:
            if random.randint(1, 52) <= 13:
                cwin += 1
print("三个人玩{0}次的模拟概率如下:".format(num))
#print("Alice   won", awin, ": Probability =", awin / num)
print("Alice   won {0} : Probability = {1}".format(awin, awin / num))
print("Bob     won", bwin, ": Probability =", bwin / num)
print("Charlie won", cwin, ": Probability =", cwin / num)


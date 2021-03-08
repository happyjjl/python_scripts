import itertools
i = 0
for a in range(8):
    for b in range(8):
        if abs(a - b) == 5 or a + b == 9:
            print (a, b)
            i += 1
print(i)

# 学而思大通关四年级第8讲第21题--传球标数法
numbers = [1, 2, 3, 4, 5]
#numbers = '12345'
all_result = list(itertools.product(numbers, repeat = 5))
i = 0
for x in all_result:
    if abs(x[0] - x[1]) == 1 and abs(x[1] - x[2]) == 1 and abs(x[2] - x[3]) == 1 and abs(x[3] - x[4]) == 1:
        i += 1
print(i)

# 学而思大通关四年级第8讲第22题--阶梯标数法
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
all_result = itertools.permutations(numbers, 8)
i = 0
for x in all_result:
    if x[4] > x[0] and x[5] > x[1] and x[6] > x[2] and x[7] > x[3] and x[1] > x[0] and x[2] > x[1] and x[3] > x[2] and x[5] > x[4] and x[6] > x[5] and x[7] > x[6]: 
        i += 1
print(i)
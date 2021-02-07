#print("Hello world")
# -*- coding: utf-8 -*-

import itertools
mylist = list(itertools.permutations([1,2,3,4,5]))

for element in mylist:
    #if (element[0] * 2 + element[1] - element[3] - element[4] * 2) == 0:
    if not element[0] * 2 + element[1] - element[3] - element[4] * 2:
        print(element)
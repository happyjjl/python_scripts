# -*- coding: utf-8 -*-
#
# 将一个正整数分解成连续的正整数之和
#
# 算法来源： https://vimsky.com/article/166.html
#
# 其他：http://mathforum.org/library/drmath/view/55979.html
#

import itertools

def find_consecutive_numbers(A):
    slow = 1
    fast = 2
    sum = 3
    begin = []
    end = []
    while slow < fast:
        if sum > A:
            sum = sum - slow
            slow = slow + 1
        else:
            if sum < A:
                fast = fast + 1
                sum = sum + fast
            else:
                begin.append(slow)
                end.append(fast)
                sum = sum - slow
                slow = slow + 1
    return (begin, end)

if __name__ == "__main__":


    pieces = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 24, 25, 28, 30]

    pieces_cuts = {4:2, 6:3, 8:4, 9:4, 10:5, 12:5, 14:7, 15:6, 16:6, 18:7, 20:7, 21:8, 24:8, 25:8, 28:9, 30:9}

    three_cakes = itertools.combinations_with_replacement(pieces, 3)
    for piece in three_cakes:
        if sum(piece) == 37:
            print(piece, pieces_cuts[piece[0]] + pieces_cuts[piece[1]] + pieces_cuts[piece[2]])

    #for i in range(n):
     #   consecutive_numbers = list(range(x[i], y[i] + 1))
        #print(y[i] - x[i] + 1, ":", x[i], y[i])
      #  print(y[i] - x[i] + 1, ":", "+".join(str(i) for i in consecutive_numbers))     
    #print("breakups:", n)
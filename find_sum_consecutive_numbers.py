# -*- coding: utf-8 -*-
#
# 将一个正整数分解成连续的正整数之和
#
# 算法来源： https://vimsky.com/article/166.html
#
# 其他：http://mathforum.org/library/drmath/view/55979.html
#


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

    N = 900
    print("divide", N, "into sum of consecutive positive numbers:")
    
    x, y = find_consecutive_numbers(N)
    n = len(x)
    
    for i in range(n):
        consecutive_numbers = list(range(x[i], y[i] + 1))
        #print(y[i] - x[i] + 1, ":", x[i], y[i])
        print(y[i] - x[i] + 1, ":", "+".join(str(i) for i in consecutive_numbers))     
    print("breakups:", n)
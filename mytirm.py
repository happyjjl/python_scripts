import math
def mytrim(s):   
    n = 0
    m = len(s) - 1
    while s[n] == ' ':
         n += 1
    while s[m] == ' ':
         m -= 1
    s = s[n:m + 1]
    return s

if __name__ == "__main__":
    s = "  abc        "
    print(mytrim(s))
    b = math.sqrt(4)
    print(b)
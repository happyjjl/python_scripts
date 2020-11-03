def isStraight(n):
    if len(set(n)) != 5:
        return False
    if 1 in n and max(n) != 5:
            n.remove(1)
            n.append(14)        # 将1替换成14
    if max(n) - min(n) == 4:
        return True
    else:
        return False 

cjj = [1,2,5,4,5]

if isStraight(cjj):
    print("yes")
else:
    print("no")
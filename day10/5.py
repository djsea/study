def max2(x, y):
    m = x if x>y else y
    return m

def max4(a,b,c,d):
    res1 = max2(a,b)
    res2 = max2(res1,c)
    res3 = max2(res2,d)
    return res3

print(max4(10,20,5,30))
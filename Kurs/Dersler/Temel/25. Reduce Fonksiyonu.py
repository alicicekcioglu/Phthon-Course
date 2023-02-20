from functools import reduce

def toplama(x,y):
    return x+y

print(reduce(toplama,[12,18,20,10]))
# 12+18 = 30
# 30+20 = 50
# 50+10 = 60

print(reduce(lambda x,y : x*y, [1,2,3,4,5]))

def maksimum(x,y):
    if x > y:
        return x
    else:
        return y

print(maksimum(5,4))

print(reduce(maksimum,[-2,3,1,4]))
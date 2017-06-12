##x = 4
##num = [4]
##for i in range(0, 50):
##    num.append((x**2)-2)
##    x = (x**2)-2
##
##y = 2
##for i in range(0, 50):
##    if num[y-2]%(2**y-1) == 0:
##        print(2**y-1)
##        y += 1
##    else:
##        y += 1

from math import *

def pc(n):
    if n>1:
        return all([n%i for i in range(2, 1 + floor(sqrt(n)))])
    else:
        return False

def ad(x,y):
    '''
    x = which input's answer to overwrite
    y = what to overwrite x with
    '''
    f = open("E:\Python\Prime Numbers\largePrime.txt", "a")
    f.write("\n\n" + str(y) +"\n" +str(x))
    f.close()

def rd(x):
    '''
    x = index of what you want to find in the list
    '''
    f = open("E:/Python/Prime Numbers/allPrime.txt", "r")
    r = f.readlines()
    r = [s.strip("\n") for s in r]
    return int(r[x])
    f.close()
    
y = int(input("Power (number in prime list): ")) #3881
while True:
    x = 4
    y += 1
    r = rd(y)
    z = 2**r-1
    for i in range(0,r):
        if x%z != 0:
            x = (x%z)**2-2
    if x%z == 0:
        ad(z,r)
        print(z)

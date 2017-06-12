from math import *

def pc(n):
    if n>1:
        return all([n%i for i in range(2, 1 + floor(sqrt(n)))])
    else:
        return False

def ad(x):
    '''
    x = what to append
    '''
    f = open("E:/Python/Prime Numbers/allPrime.txt", "a")
    f.write(str(x) + "\n")
    f.close()

x = int(input("Number: "))
while True:
    if pc(x) == True:
        ad(x)
    x += 2

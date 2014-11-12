def zeros(n):
    return howmanyfives(long(n))

def howmanyfives(n):
    fives=0
    i=1
    while n/(5**i)>=1:
        fives+=int(n/(5**i))
        i+=1
    return fives

print zeros(1000000000000000)

#the following two solution not support too too big number because of ram limit
"""
------------%ver---------------
import sys
sys.setrecursionlimit(1000000000)
def zeros(n):
    result=extratimes(long(n))
    zero=0
    if result%10!=0:
        return zero
    else:
        while result%(10**(zero+1))==0:
            zero+=1
        return zero
def extratimes(n):
    n=long(n)
    if n==1:
        return 1
    else:
        print long(n)
        return extratimes(long(n)-1L)*long(n)
    
print zeros(100000)
"""

"""
------string ver---------
import sys
sys.setrecursionlimit(26191)
#use sys.setrecursionlimit to make recursion be able to go through 1000
def zeros(n):
    result=str(extratimes(long(n)))
    #use long() to support super long number
    zero=0
    if result[-1]!='0':
        return zero
    else:
        while (result[-zero-1]=='0'):
            zero+=1
        return zero
def extratimes(n):
    n=long(n)
    if n==1:
        return 1
    else:
        return extratimes(n-1L)*n
"""
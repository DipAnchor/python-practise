import random
str0=("35953605")

nums=raw_input("numbers U want:\n")

for i in range(1,int(nums)):
    lsnum=random.randint(234567,8876543)
    if lsnum<1000000:
        result=('0'+str(lsnum))
    else:
        result=str(lsnum)    
    print str0+result
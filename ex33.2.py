#coding:utf-8

def countnum(num):
    numbers=[]
    for i in range(1,int(num)+1):
        if i!=0:
            print ("Numbers now:",numbers)
            print ("At the bottom i is %d \n"%i)
        print ("At the top i is %d" %i)
        numbers.append(i)
    print("The numbers:")

    for num in numbers:
        print num

num=raw_input("Your numbers:>\n")
countnum(int(num))
#this code not work
class mstack:
    def __init__(self):
        self.list=[]
    def pop(self):
        return self.list.pop()
    def push(self,x):
        return self.list.append(x)
    def top(self):
        print "top is>"
        return self.list[-1]
    def getMin(self):
        min=self.list[0]
        for i in xrange(0,len(self.list),1):
            min=self.list[i] and min>self.list[i] or min
        print "min is %d>"%min
        return min

while(True):
    newtype=mstack()
    action=0
    action=raw_input("""
    please chose a function:
        1.pop
        2.push
        3.top
        4.getMin
        >"""
    )
    if action=='1':newtype.pop()
    if action=='2':newtype.push(raw_input('Input number U want to push>'))
    if action=='3':print newtype.top()
    if action=='4':print newtype.getMin()

    
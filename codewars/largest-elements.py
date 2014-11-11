def largest(n,xs):
    "Find the n highest elements in a list"
    xs.sort()
    return xs[(len(xs)-n):]
    #while len(xs)>n:
    #    xs.pop(0)
    #return xs

print largest(3,[5,1,5,2,3,1,2,3,5])
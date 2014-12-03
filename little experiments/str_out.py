import ast

str="""(u'one',{u'a':u"1",u'b':u'2'}) (u'two',{u'ass':u"f1",u'cb':u'2df'})"""



lindex=[]
rindex=[]
result=[]
results=[]

for n in xrange(0,len(str)):
    if str[n]=='{':
        lindex.append(n)
    elif str[n]=='}':
        rindex.append(n)

for i in xrange(0,len(lindex)):
    result.append(str[lindex[i]:rindex[i]+1])

for k in result:
    results.append(ast.literal_eval(k))

print results
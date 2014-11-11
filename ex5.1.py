#coding:utf8
import sys
print sys.getdefaultencoding()
str1='您好'
str=u'您好'
print repr(str1)
print repr(str)
print str1
print str.encode('gbk')
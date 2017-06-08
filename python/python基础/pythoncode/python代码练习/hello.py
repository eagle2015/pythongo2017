#!/usr/bin/python
#coding:utf-8

str = 'Hello python！2017\t'
print str # 输出完整字符串
print str[0] # 输出字符串中的第一个字符
print len(str)
print str[6:12] # 输出字符串中第6个至第12个之间的字符串
print str[2:] # 输出从第三个字符开始的字符串
print str * 2 # 输出字符串两次
print str + "TEST" # 输出连接的字符串
print str[6:-5]  #截取中间部分


'''
结果：
Hello python！2017
H
20
python
llo python！2017
Hello python！2017	Hello python！2017
Hello python！2017	TEST
python！
'''


#list
list = ['flying', 86, 12.23, 'eagle', 170,.2]
tinylist = [123, 'bat']

print list  # 输出完整列表
print list[0]  # 输出列表的第一个元素
print list[1:3]  # 输出第二个至第三个的元素
print list[2:]  # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2  # 输出列表两次
print list + tinylist  # 打印组合的列表


#可以用来遍历一个序列
name = ['flying','eagle','python','go','bat','a','b','t']
for name in  range(0,len(name)):
    print "##"* name,name



tuple =('flying', 86, 1.1, 'eagle', 1.70, 2.2)
tinylist = (1, 'bat')
print tuple # 输出完整列表
print tuple[0] # 输出列表的第一个元素
print tuple[1:3] # 输出第二个至第三个的元素
print tuple[2:] # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2 # 输出列表两次
print tuple + tinylist # 打印组合的列表
print "tuple lenth:" ,len(tuple)
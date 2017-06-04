#!/usr/bin/env python
#coding:utf-8


x = raw_input('please enter you name:')
y = raw_input('please enter your age: ')

if x == 'flying':
    if y == '27':
        print "%s %s is old" % (x, y)
    elif y == '10':
        print  "%s %s is young" % (x, y)
    else:
        print 'I don"n know'
else:
    print 'not an age'



for name in ['tengine','flying','eagle','python','go']:
            print name

name = ['tengine','flying','eagle','python','go','bat','b','a','t']
for num in  range(0,len(name)):
    print "##"* num,
    if num == 7:
        break
    print num, name


#continue  可以跳出当前这一次循环，从下次开始继续循环（for，while）
for num in range(5, 15):
    if num == 9:
        # num等于7的时候，结束当前循环，继续下一次循环，所以8.9还会打印出来
        continue
    print num


flag = False
name = 'flying'

if name == 'python':  # 判断变量否为'python'
    flag = True  # 条件成立时设置标志为真
    print 'welcome boss'  # 并输出欢迎信息
else:
    print name  # 条件不成立时输出变量名称

num = raw_input("please in numble:")
if num == 13:            # 判断num的值
    print 'boss'
elif num == 12:
    print 'user'
elif num == 1:
    print 'worker'
elif num < 0:           # 值小于零时输出
    print 'error'
else:
    print 'roadman'     # 条件均不成立时输出

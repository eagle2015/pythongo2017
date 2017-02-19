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




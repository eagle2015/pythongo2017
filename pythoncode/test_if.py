#!/usr/bin/env python

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


for num in range(0, 20):
    print num



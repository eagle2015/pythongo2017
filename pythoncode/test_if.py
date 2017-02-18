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

name = ['tengine','flying','eagle','python','go']
for name in  range(0,len(name)):
    print "##"* name,name



for num in range(0, 20):
    print num



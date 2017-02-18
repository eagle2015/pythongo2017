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
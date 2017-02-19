#!/usr/bin/python
#coding:utf-8

a = 20
b = 16
c = 30

c = a + b
print "a + b = ", c

c = a - b
print "a - b = ", c

c = a * b
print "a *b = ", c

c = a / b
print "a / b = ", c

c = a % b
print "a % b = ", c

a = 2
b = 3
c = a ** b
print "a ** b = ", c

a = 10
b = 5
c = a // b
print "a // b = ", c

'''
a + b =  36
a - b =  4
a *b =  320
a / b =  1
a % b =  4
a ** b =  8
a // b =  2

'''


if (a == b):
    print "Line 1 - a is equal to b"
else:
    print "Line 1 - a is not equal to b"

if (a != b):
    print "Line 2 - a is not equal to b"
else:
    print "Line 2 - a is equal to b"

if (a <> b):
    print "Line 3 - a is not equal to b"
else:
    print "Line 3 - a is equal to b"

if (a < b):
    print "Line 4 - a is less than b"
else:
    print "Line 4 - a is not less than b"

if (a > b):
    print "Line 5 - a is greater than b"
else:
    print "Line 5 - a is not greater than b"

a = 25;
b = 220;
if (a <= b):
    print "Line 6 - a is either less than or equal to  b"
else:
    print "Line 6 - a is neither less than nor equal to  b"

if (b >= a):
    print "Line 7 - b is either greater than  or equal to b"
else:
    print "Line 7 - b is neither greater than  nor equal to b"


    '''

Line 1 - a is not equal to b
Line 2 - a is not equal to b
Line 3 - a is not equal to b
Line 4 - a is not less than b
Line 5 - a is greater than b
Line 6 - a is either less than or equal to  b
Line 7 - b is either greater than  or equal to b
    '''

a = 20
b = 16
c = 30
c = a + b
print "Line 1 - Value of c is: ", c

c += a
print "Line 2 - Value of c is: ", c

c *= a
print "Line 3 - Value of c is: ", c

c /= a
print "Line 4 - Value of c is: ", c

c = 2
c %= a
print "Line 5 - Value of c is: ", c

c **= a
print "Line 6 - Value of c is: ", c

c //= a
print "Line 7 - Value of c is: ", c


'''
Line 1 - Value of c is:  36
Line 2 - Value of c is:  56
Line 3 - Value of c is:  1120
Line 4 - Value of c is:  56
Line 5 - Value of c is:  2
Line 6 - Value of c is:  1048576
Line 7 - Value of c is:  52428
'''

c = a & b;  # 12 = 0000 1100
print "Line 1 - Value of c is ", c

c = a | b;  # 61 = 0011 1101
print "Line 2 - Value of c is ", c

c = a ^ b;  # 49 = 0011 0001
print "Line 3 - Value of c is ", c

c = ~a;  # -61 = 1100 0011
print "Line 4 - Value of c is ", c

c = a << 2;  # 240 = 1111 0000
print "Line 5 - Value of c is ", c

c = a >> 2;  # 15 = 0000 1111
print "Line 6 - Value of c is ", c

'''
Line 1 - Value of c is  16
Line 2 - Value of c is  20
Line 3 - Value of c is  4
Line 4 - Value of c is  -21
Line 5 - Value of c is  80
Line 6 - Value of c is  5
'''

if (a and b):
    print "Line 1 - a and b are true"
else:
    print "Line 1 - Either a is not true or b is not true"

if (a or b):
    print "Line 2 - Either a is true or b is true or both are true"
else:
    print "Line 2 - Neither a is true nor b is true"

a = 0
if (a and b):
    print "Line 3 - a and b are true"
else:
    print "Line 3 - Either a is not true or b is not true"

if (a or b):
    print "Line 4 - Either a is true or b is true or both are true"
else:
    print "Line 4 - Neither a is true nor b is true"

if not (a and b):
    print "Line 5 - a and b are true"
else:
    print "Line 5 - Either a is not true or b is not true"

    '''
Line 1 - a and b are true
Line 2 - Either a is true or b is true or both are true
Line 3 - Either a is not true or b is not true
Line 4 - Either a is true or b is true or both are true
Line 5 - a and b are true
    '''

list = [1, 2, 3, 4, 5,20,33,30];

if (a in list):
    print "Line 1 - a is available in the given list"
else:
    print "Line 1 - a is not available in the given list"

if (b not in list):
    print "Line 2 - b is not available in the given list"
else:
    print "Line 2 - b is available in the given list"

c = 33
if (c in list):
    print "Line 3 - c is available in the given list"
else:
    print "Line 3 - c is not available in the given list"

'''
Line 1 - a is not available in the given list
Line 2 - b is not available in the given list
Line 3 - c is available in the given list
'''
d = 10
if (a is d):
    print "Line 1 - a and b have same identity"
else:
    print "Line 1 - a and b do not have same identity"

if (id(a) == id(b)):
    print "Line 2 - a and b have same identity"
else:
    print "Line 2 - a and b do not have same identity"

a = 22
b = 22
if (a is b):
    print "Line 3 - a and b have same identity"
else:
    print "Line 3 - a and b do not have same identity"

if (a is not b):
    print "Line 4 - a and b do not have same identity"
else:
    print "Line 4 - a and b have same identity"

'''
is	是判断两个标识符是不是引用自一个对象	x is y, 如果 id(x) 等于 id(y) , is 返回结果 1
is not是判断两个标识符是不是引用自不同对象	x is not y, 如果 id(x) 不等于 id(y). is not 返回结果 1

Line 1 - a and b do not have same identity
Line 2 - a and b do not have same identity
Line 3 - a and b have same identity
Line 4 - a and b have same identity
'''

a = 20
b = 10
c = 15
d = 5
e = 0

e = (a + b) * c / d  # ( 30 * 15 ) / 5
print "Value of (a + b) * c / d is :", e

e = ((a + b) * c) / d  # (30 * 15 ) / 5
print "Value of ((a + b) * c) / d is :", e

e = (a + b) * (c / d);  # (30) * (15/5)
print "Value of (a + b) * (c / d) is: ", e

e = a + (b * c) / d;  # 20 + (150/5)
print "Value of a + (b * c) / d is :", e


'''
Value of (a + b) * c / d is : 90
Value of ((a + b) * c) / d is : 90
Value of (a + b) * (c / d) is:  90
Value of a + (b * c) / d is : 50

'''
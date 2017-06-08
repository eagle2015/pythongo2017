#!/usr/bin/python
#coding:utf-8


for num in range(11,20):  #to iterate between 11 to 20
   for i in range(2,num): #to iterate on the factors of the number
      if num%i == 0:      #to determine the first factor
         j=num/i          #to calculate the second factor
         print '%d equals = %d * %d' % (num,i,j)
         break #to move to the next number, the #first FOR
   else:                  # else part of the loop
      print num, 'is a prime number'


i = 1
while (i < 50):
    j = 2
    while (j <= (i / j)):
        if not (i % j): break
        j = j + 1
    if (j > i / j): print i, " 是素数"
    i = i + 1

print "Good bye! python 2017!"

for letter in 'Python':  # First Example
    if letter == 'o':
        break
    print 'Current Letter :', letter

var = 100  # Second Example
while var > 0:
    var = var - 10
    if var == 60:
        continue
    elif var == 20:
        break
    print 'Current variable value :', var
print "Good bye!python 2017"


'''

Current Letter : P
Current Letter : y
Current Letter : t
Current Letter : h
Current variable value : 90
Current variable value : 80
Current variable value : 70
Current variable value : 50
Current variable value : 40
Current variable value : 30
Good bye!python 2017
'''
L = ('flying', 'Flying', 'eagle!','fly',"Eagle")
print  L[2]   #读取第三个元素
print L[-2]   #反向读取；读取倒数第二个元素
print L[1:]    #截取元素
print L[1:-1]

'''
eagle!
fly
('Flying', 'eagle!', 'fly', 'Eagle')
('Flying', 'eagle!', 'fly')
'''

print 'abc', -14.24e93, 18+16.6j, 'xyz';
x, y = 10, 20;
print "Value of x , y : ", x,y;
'''
#===========================================
#abc -1.424e+94 (18+16.6j) xyz
#Value of x , y :  10 20
'''


tuple1, tuple2 = (123, 'xyz', 'flying', 'abc'), (456, 200, 300)
print "Max value element : ", max(tuple1);
print "Max value element : ", max(tuple2);


'''
Max value element :  xyz
Max value element :  456
'''

print "min value element : ", min(tuple1);
print "min value element : ", min(tuple2);

aList = [123, 'eagle', 'flying', 'bat'];
aTuple = tuple(aList)

print "Tuple elements : ", aTuple



aList = [123, 'eagle', 'flying', 'bat'];
list = [123, 'eagle', 'flying', 'bat']
print "Value available at index 0 : "
print "list[0]:", list[0];
list[0] = 2001;
print "New value available at index 0 : "
print "list[0]:",list[0];
aList.append(2017)
print "aList:",aList
list.append(2016)
list.append(2017)
list[0]= 2019
print "list:",list
del list[3]
print "new list:",list

aList = [123, 'eagle', 'flying', 'bat'];
for i in aList:
    print "aList:",i

app_list =  [2019, 'eagle', 'flying', 'bat', 2016, 2017]
for app_id in app_list:
    print "1 app_list:",app_id

for index,app_id in enumerate(app_list):
    print "2 app_list[%s] " % index, app_id

for index in range(len(app_list)):
    print "3 app_list[%s]: " % index, app_list[index]

for app_id in iter(app_list):
    print "4 app_list:",app_id



a=[111,222,13,24,535,656,747,848,99,590]
dict1={'k1':[],'k2':[]}

for i in a:
    if i >66:
        dict1['k1'].append(i)
    else:
        dict1['k2'].append(i)
print dict1

#最好的是用下面的方法来动态的扩展字典：
a=[111,222,133,414,551,663,737,838,929,920]
dict1={}  #动态的增加字典

for i in a:
    if i >662:
        if 'k1' in dict1.keys():
            dict1['k1'].append(i)
        else:
            dict1['k1'] = [i,]
    else:
        if 'k2' in dict1.keys():
            dict1['k2'].append(i)
        else:
            dict1['k2'] = [i,]
print "dict1:",dict1


'''

{'k2': [13, 24], 'k1': [111, 222, 535, 656, 747, 848, 99, 590]}
dict1: {'k2': [111, 222, 133, 414, 551], 'k1': [663, 737, 838, 929, 920]}
'''
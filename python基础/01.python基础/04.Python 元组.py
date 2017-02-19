 一 Python 元组
创建空元组
二访问元组
三修改元组
四删除元组
五元组运算符
六元组索引截取
七无关闭分隔符
八元组内置函数
一Python Tuple元组 cmp方法
二Python Tuple元组 len方法
三Python Tuple元组 max方法
四Python Tuple元组 min方法
五Python Tuple元组 tuple方法

 一、Python 元组
    Python的元组与列表类似，不同之处在于元组的元素不能修改。
元组使用小括号，列表使用方括号。
元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
如下实例：
 tup1 = ('physics', 'chemistry', 2017, 2018);
 tup2 = (1, 2, 3, 4, 5 );

1、创建空元组  :
 tup1 = ();
元组中只包含一个元素时，需要在元素后面添加逗号   :tup1 = (50,);
元组与字符串类似，下标索引从0开始，可以进行截取，组合等。

二、访问元组
元组可以使用下标索引来访问元组中的值，如下实例:
 '''
tup1 = ('flying', 'eagle', 2017, 2018);
tup2 = (1, 2, 3, 4, 5, 6, 7 );

print "tup1[0]: ", tup1[0]
print "tup1[1]: ", tup1[1]
print "tup2[1:5]: ", tup2[1:5]
 '''

三、修改元组
元组中的元素值是不允许修改的，但我们可以对元组进行连接组合，如下实例:

 '''
 #!/usr/bin/python

tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');

# 以下修改元组元素操作是非法的。
# tup1[0] = 100;

# 创建一个新的元组
tup3 = tup1 + tup2;
print tup3;
 '''

'''
(12, 34.56, 'abc', 'xyz')
'''

四、删除元组
元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组，如下实例:  # !/usr/bin/python
   '''
  tuple1 = ('flying', 'eagle', 2017, 2018);

  print tuple1;
  del tuple1;
  print "After deleting tup : "
  print tuple1;
  '''

以上实例元组被删除后，输出变量会有异常信息，输出如下所示：

 '''
 ('flying', 'eagle', 2017, 2018)
 After deleting tup :
Traceback (most recent call last):
  File "test.py", line 9, in <module>
    print tuple1;
NameError: name 'tuple1' is not defined
 '''


五、元组运算符
与字符串一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组。
Python 表达式	        结果	                     描述
len((1, 2, 3))	         3	                        计算元素个数
(1, 2, 3) + (4, 5, 6)	(1, 2, 3, 4, 5, 6)	        连接
['Hi!'] * 4	('Hi!', 'Hi!', 'Hi!', 'Hi!')	        复制
3 in (1, 2, 3)	True	                            元素是否存在
for x in (1, 2, 3): print x,	1 2 3	            迭代

六、元组索引，截取
因为元组也是一个序列，所以我们可以访问元组中的指定位置的元素，也可以截取索引中的一段元素，如下所示：
元组：
Python 表达式	结果	描述
L = ('flying', 'Flying', 'eagle!','fly',"Eagle")
print  L[2]   #读取第三个元素
print L[-2]   #反向读取；读取倒数第二个元素
print L[1:]    #截取元素
print L[1:-1]

eagle!
fly
('Flying', 'eagle!', 'fly', 'Eagle')
('Flying', 'eagle!', 'fly')

七、无关闭分隔符
任意无符号的对象，以逗号隔开，默认为元组，如下实例：
'''
#!/usr/bin/python

print 'abc', -14.24e93, 18+16.6j, 'xyz';
x, y = 10, 20;
print "Value of x , y : ", x,y;
'''
===================================
abc -1.424e+94 (18+16.6j) xyz
Value of x , y :  10 20
 ==================================

八、元组内置函数
Python元组包含了以下内置函数

序号	方法及描述
1	cmp(tuple1, tuple2)  比较两个元组元素。
2	len(tuple)   计算元组元素个数。
3	max(tuple)  返回元组中元素最大值。
4	min(tuple)  返回元组中元素最小值。
5	tuple(seq)   将列表转换为元组。

（一）Python Tuple(元组) cmp()方法
1、描述
Python 元组 cmp() 函数用于比较两个元组元素。
2、语法
cmp()方法语法：cmp(tuple1, tuple2)

3、参数
tuple1 -- 比较的元组。
tuple2 -- 比较的另外一个元组。

4.返回值
（1）如果比较的元素是同类型的,则比较其值,返回结果。
（2）如果两个元素不是同一种类型,则检查它们是否是数字。
如果是数字,执行必要的数字强制类型转换,然后比较。
如果有一方的元素是数字,则另一方的元素"大"(数字是"最小的")
否则,通过类型名字的字母顺序进行比较。
（3）如果有一个列表首先到达末尾,则另一个长一点的列表"大"。
（4）如果我们用尽了两个列表的元素而且所 有元素都是相等的,那么结果就是个平局,就是说返回一个 0



'''
#!/usr/bin/python

tuple1, tuple2 = (123, 'xyz'), (456, 'abc')

print cmp(tuple1, tuple2);
print cmp(tuple2, tuple1);
tuple3 = tuple2 + (786,);
print cmp(tuple2, tuple3)
'''
=====================
-1
1
-1
=====================


（二）Python Tuple(元组) len()方法
1、描述
Python 元组 len() 函数计算元组元素个数。
2、语法
len()方法语法：
len(tuple1, tuple2)

3、参数
tuple -- 要计算的元组。
4、返回值
函数返回元组元素个数。

 '''
 #!/usr/bin/python

tuple1, tuple2 = (123, 'xyz', 'zara'), (456, 'abc')

print "First tuple length : ", len(tuple1);
print "Second tuple length : ", len(tuple2);
 '''

 ======================
First tuple length :  3
Second tuple length :  2
 =======================

（三）Python Tuple(元组) max()方法
1、描述:Python 元组 max() 函数返回元组中元素最大值。
2、语法:max()方法语法：max(tuple)
 3、参数:tuple -- 指定的元组。
4、返回值:返回元组中元素最大值。
5、实例:以下实例展示了 max()函数的使用方法：
 '''
#!/usr/bin/python

tuple1, tuple2 = (123, 'xyz', 'flying', 'abc'), (456, 200, 300)
print "Max value element : ", max(tuple1);
print "Max value element : ", max(tuple2);
'''
'''
Max value element :  xyz
Max value element :  456
'''

（四）Python Tuple(元组) min()方法
1、描述:Python 元组 min() 函数返回元组中元素最小值。
2、语法:min()方法语法：min(tuple)
3、参数:tuple -- 指定的元组。
4、返回值:返回元组中元素最小值。
5、实例:以下实例展示了 min()函数的使用方法：

print "min value element : ", min(tuple1);
print "min value element : ", min(tuple2);

min value element :  123
min value element :  200

（五）Python Tuple(元组) tuple()方法
1、描述:Python 元组 tuple() 函数将列表转换为元组。
2、语法: tuple()方法语法：tuple( seq )
3、参数:seq -- 要转换为元组的序列。
4、返回值:返回元组中元素最小值。
5、实例:以下实例展示了 tuple()函数的使用方法：

 aList = [123, 'eagle', 'flying', 'bat'];
 aTuple = tuple(aList)

 print "Tuple elements : ", aTuple

Tuple elements :  (123, 'eagle', 'flying', 'bat')




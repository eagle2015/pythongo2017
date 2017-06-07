Python基本语法

一 第一个Python程序
交互式编程
脚本式编程
二Python标识符
三Python保留字符
四Python的行和缩进
五Python的多行语句
六Python 引号
七Python注释
八Python的空行
九Python实现等待用户输入
十Python同一行显示多条语句
十一Python多个语句构成代码组
十二Python命令行参数

一、第一个Python程序
1、交互式编程
所谓交互式编程，就是不通过脚本文件作为参数使用 Python 解释器的交互模式，提示窗口如下：
 python
Python 2.7 (r27:82500, Jun 18 2014, 17:22:01)
[GCC 4.1.2 20080704 (Red Hat 4.1.2-54)] on linux2
Type "help", "copyright", "credits" or "license" for more information.

    2、脚本式编程
    所谓脚本是编程，就是通过脚本参数调用解释器开始执行脚本，直到脚本执行完毕。当脚本执行完成后，解释器不再有效。
  python dic.py

    二、Python标识符
    关于Python标识符，需要注意以下几点：
    1、在python里，标识符有字母、数字、下划线组成。
    2、在python中，所有标识符可以包括英文、数字以及下划线（_），但不能以数字开头。
    3、在python中，标识符是区分大小写的。
    4、在python中，以下划线开头的标识符是有特殊意义的。
以单下划线开头（_foo）的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用"from xxx import *"而导入；
    5、在python中，以双下划线开头的（__foo）代表类的私有成员；以双下划线开头和结尾的（__foo__）代表python里特殊方法专用的标识，如__init__（）代表类的构造函数。

    三、Python保留字符
    下面的列表显示了在Python中的保留字。这些保留字不能用作常数或变数，或任何其他标识符名称。
    注意：所有Python的关键字只包含小写字母。
    and  exec not assert    finally or break  for pass class from print continue global raise
    def if return del import try elif in while else is with except    lambda yield

    四、Python的行和缩进
     学习Python与其他语言最大的区别就是，Python的代码块不使用大括号（{}）来控制类，函数以及其他逻辑判断。python最具特色的就是用缩进来写模块。
     缩进的空白数量是可变的，但是所有代码块语句必须包含相同的缩进空白数量，这个必须严格执行。

在Python的代码块中必须使用相同数目的行首缩进空格数。

五、Python的多行语句
        Python语句中一般以新行作为为语句的结束符。但是我们也可以使用斜杠（ \）将一行的语句分为多行显示，如下所示：
'''
total = item_one + \
       item_two + \
       item_three
'''

语句中包含[], {} 或 () 括号就不需要使用多行连接符。如下实例：
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']

六、Python 引号
Python 接收单引号(' )，双引号(" )，三引号(''' """) 来表示字符串，引号的开始与结束必须的相同类型的。
其中三引号可以由多行组成，编写多行文本的快捷语法，常用语文档字符串，在文件的特定地点，被当做注释。

七、Python注释
1、在python中单行注释采用 # 开头。
2、python没有块注释，所以现在推荐的多行注释也是采用的 #。



八、Python的空行
       函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
       空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。
       但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。
       记住：空行也是程序代码的一部分。

九、Python实现等待用户输入
下面的程序在按回车键后就会等待用户输入:raw_input

#!/usr/bin/python

raw_input("\n\nPress the enter key to exit.")


十、Python同一行显示多条语句
Python可以在同一行中使用多条语句，语句之间使用分号(;)分割。
以下是一个简单的实例：

import sys; x = 'foo'; sys.stdout.write(x + '\n')

十一、Python多个语句构成代码组
        缩进相同的一组语句构成一个代码块，我们称之代码组。像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
        我们将首行及后面的代码组称为一个子句(clause)。
如下实例：if

if expression :
   suite
elif expression :
   suite
else :
   suite

十二、Python命令行参数
很多程序可以执行一些操作来查看一些基本信息，Python可以使用-h参数查看各参数帮助信息：




Python变量类型

一Python 变量类型简介
Python中变量的特点
关于变量类型需要注意以下几点
二变量赋值
三多个变量赋值
四标准数据类型
五Python数字
数字数据类型用于存储数值
Python支持四种不同的数值类型
实例
六Python字符串
字符串或串String是由数字字母下划线组成的一串字符
python的字串列表有2种取值顺序
实例
七Python列表
八Python元组
九Python元字典
十Python数据类型转换

一、Python 变量类型简介
1、Python中变量的特点：
我们知道，在Python中，变量有如下的特点：
（1）变量不需要声明
Python的变量不需要声明，你可以直接输入：

>>>a = 10

内存里就有了一个变量a， 它的值是10，它的类型是integer (整数)。 在此之前你不需要做什么特别的声明，而数据类型是Python自动决定的。

>>>print a
>>>print type(a)
10
<type 'int'>


内置函数type(), 用以查询变量的类型。

（2）回收变量名
如果你想让a存储不同的数据，你不需要删除原有变量就可以直接赋值。
>>>a = 1.31
>>>print a,type(a)
1.31<type 'float'>

print a,type(a)
print的另一个用法，也就是print后跟多个输出，以逗号分隔。

在Python中，变量不需要声明，不需要删除，可以直接回收适用。type()用于查询数据类型

2、关于变量类型需要注意以下几点：
（1）变量存储在内存中的值。这就意味着在创建变量时会在内存中开辟一个空间。
（2）基于变量的数据类型，解释器会分配指定内存，并决定什么数据可以被存储在内存中。
因此，变量可以指定不同的数据类型，这些变量可以存储整数，小数或字符。

二、变量赋值
在Python中，变量赋值需要注意以下几点：
1、Python中的变量不需要声明，变量的赋值操作既是变量声明和定义的过程。
2、每个变量在内存中创建，都包括变量的标识，名称和数据这些信息。
3、每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
4、等号（=）用来给变量赋值。
5、等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。
例子：
'''
dict =  {'age': 27, 'Work': 'PE', 'Name': 'fly', 'Sex': 'female'}
print "#"*7,"dict","#"*7
for key in dict:
    print "dict[%s]:" % key,dict[key]

'''

三、多个变量赋值
Python允许同时为多个变量赋值。

>>> a = b =c = 10
>>> print id(a),id(b),id(c)
213202640 213202640 213202640

创建一个整型对象，值为10三个变量被分配到相同的内存空间上。通过下面的方法可以查看到3个变量分配的内存空间：print id(a),id(b),id(c)

也可以为多个对象指定多个变量。例如：

>>> a, b, c = 1, 2, "flying"
>>> print a,b,c
1 2 flying
两个整型对象1和2的分配给变量a和b，字符串对象"flying“ 分配给变量c


四、标准数据类型
在内存中存储的数据可以有多种类型。
例如，person.s年龄作为一个数值存储和他或她的地址是字母数字字符存储。
Python有一些标准类型用于定义操作上，他们和为他们每个人的存储方法可能。
Python有五个标准的数据类型：
1、Numbers（数字）
2、String（字符串）
3、List（列表）
4、Tuple（元组）
5、Dictionary（字典）

五、Python数字
1、数字数据类型用于存储数值。
他们是不可改变的数据类型，这意味着改变数字数据类型会分配一个新的对象。
当你指定一个值时，Number对象就会被创建：

var1 = 11
var2 = 101
您也可以使用del语句删除一些对象引用。
del语句的语法是：del var1[,var2[,var3[....,varN]]]]

您可以通过使用del语句删除单个或多个对象。例如：
del var
del var_a, var_b

2、Python支持四种不同的数值类型：
（1）int（有符号整型）
（2）long（长整型[也可以代表八进制和十六进制]）
（3）float（浮点型）
（4）complex（复数）
3、实例
一些数值类型的实例
注意：
（1）长整型也可以使用小写"L"，但是还是建议您使用大写"L"，避免与数字"1"混淆。Python使用"L"来显示长整型。
（2）Python还支持复数，复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型
 int	long	float	complex
10	51924361L	0.0	3.14j
100	-0x19323L	15.20	45.j
-786	0122L	-21.9	9.322e-36j
080	0xDEFABCECBDAECBFBAEl	32.3+e18	.876j
-0490	535633629843L	-90.	-.6545+0J
-0x260	-052318172735L	-32.54e100	3e+26J
0x69	-4721885298529L	70.2-E12	4.53e-7j


六、Python字符串
1、字符串或串(String)是由数字、字母、下划线组成的一串字符。
它是编程语言中表示文本的数据类型。

2、python的字串列表有2种取值顺序:
（1）从左到右索引默认0开始的，最大范围是字符串长度少1
（2）从右到左索引默认-1开始的，最大范围是字符串开头
如果你的实在要取得一段子串的话，可以用到变量[头下标:尾下标]，就可以截取相应的字符串，其中下标是从0开始算起，可以是正数或负数，下标可以为空表示取到头或尾。
比如:

s = 'ilovepython'
s[1:5]的结果是love。
当使用以冒号分隔的字符串，python返回一个新的对象，结果包含了以这对偏移标识的连续的内容，左边的开始是包含了下边界。
上面的结果包含了s[1]的值l，而取到的最大范围不包括上边界，就是s[5]的值p。
加号（+）是字符串连接运算符，星号（*）是重复操作。


3、实例：
#!/usr/bin/python

str = 'Hello python！'
print str # 输出完整字符串
print str[0] # 输出字符串中的第一个字符
print str[2:5] # 输出字符串中第三个至第五个之间的字符串
print str[2:] # 输出从第三个字符开始的字符串
print str * 2 # 输出字符串两次
print str + "TEST" # 输出连接的字符串



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

七、Python列表
List（列表） 是 Python 中使用最频繁的数据类型。
关于列表需要注意的事项如下：
1、列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（所谓嵌套）；
2、列表用[ ]标识。是python最通用的复合数据类型；
3、列表中的值得分割也可以用到变量[头下标:尾下标]，就可以截取相应的列表，从左到右索引默认0开始的，从右到左索引默认-1开始，下标可以为空表示取到头或尾。
4、加号（+）是列表连接运算符，星号（*）是重复操作。

#list
list = ['flying', 86, 12.23, 'eagle', 170,.2]
tinylist = [123, 'john']

print list  # 输出完整列表
print list[0]  # 输出列表的第一个元素
print list[1:3]  # 输出第二个至第三个的元素
print list[2:]  # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2  # 输出列表两次
print list + tinylist  # 打印组合的列表


['flying', 86, 12.23, 'eagle', 170, 0.2]
flying
[86, 12.23]
[12.23, 'eagle', 170, 0.2]
[123, 'john', 123, 'john']
['flying', 86, 12.23, 'eagle', 170, 0.2, 123, 'john']

可以用来遍历一个序列
name = ['flying','eagle','python','go','bat','a','b','t']
for name in  range(0,len(name)):
    print "##"* name,name

八、Python元组
元组是另一个数据类型，类似于List（列表）。元组用"()"标识。内部元素用逗号隔开。但是元素不能二次赋值，相当于只读列表。

tuple =('flying', 86, 1.1, 'eagle', 1.70, 2.2)
tinylist = (1, 'bat')
print tuple # 输出完整列表
print tuple[0] # 输出列表的第一个元素
print tuple[1:3] # 输出第二个至第三个的元素
print tuple[2:] # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2 # 输出列表两次
print tuple + tinylist # 打印组合的列表
print "tuple lenth:" ,len(tuple)


元组是不允许更新的。而列表是允许更新的





九 Python数据类型转换

数据类型的转换，你只需要将数据类型作为函数名即可。
以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。

int(x [,base])将x转换为一个整数
long(x [,base] )将x转换为一个长整数
float(x)将x转换到一个浮点数
complex(real [,imag])创建一个复数
str(x)将对象 x 转换为字符串
repr(x)将对象 x 转换为表达式字符串
eval(str)用来计算在字符串中的有效Python表达式,并返回一个对象
tuple(s)将序列 s 转换为一个元组
list(s)将序列 s 转换为一个列表
set(s)转换为可变集合
dict(d)创建一个字典。d 必须是一个序列 (key,value)元组。
frozenset(s)转换为不可变集合
chr(x)将一个整数转换为一个字符
unichr(x)将一个整数转换为Unicode字符
ord(x)将一个字符转换为它的整数值
hex(x)将一个整数转换为一个十六进制字符串
oct(x)将一个整数转换为一个八进制字符串



set集合

set是一个无序且不重复的元素集合

python的set和其他语言类似, 是一个无序不重复元素集, 基本功能包括关系测试和消除重复元素.
集合对象还支持union(联合), intersection(交), difference(差)和sysmmetric difference(对称差集)等数学运算.

sets 支持 x in set, len(set),和 for x in set。作为一个无序的集合，sets不记录元素位置或者插入点。
因此，sets不支持 indexing, slicing, 或其它类序列（sequence-like）的操作。



下面来点简单的小例子说明把。

>>> x = set('spam')
>>> y = set(['h','a','m'])
>>> x, y
(set(['a', 'p', 's', 'm']), set(['a', 'h', 'm']))

再来些小应用。

>>> x & y # 交集
set(['a', 'm'])

>>> x | y # 并集
set(['a', 'p', 's', 'h', 'm'])

>>> x - y # 差集
set(['p', 's'])

记得以前个网友提问怎么去除海量列表里重复元素，用hash来解决也行，只不过感觉在性能上不是很高，用set解决还是很不错的，示例如下：

>>> a = [11,22,33,44,11,22]
>>> b = set(a)
>>> b
set([33, 11, 44, 22])
>>> c = [i for i in b]
>>> c
[33, 11, 44, 22]
很酷把，几行就可以搞定。
1.8　集合

集合用于包含一组无序的对象。要创建集合，可使用set()函数并像下面这样提供一系列的项：
s = set([3,5,9,10])      #创建一个数值集合
t = set("Hello")         #创建一个唯一字符的集合
与列表和元组不同，集合是无序的，也无法通过数字进行索引。此外，集合中的元素不能重复。例如，如果检查前面代码中t集合的值，结果会是：

>>> t
set(['H', 'e', 'l', 'o'])
注意只出现了一个'l'。

集合支持一系列标准操作，包括并集、交集、差集和对称差集，例如：
a = t | s          # t 和 s的并集
b = t & s          # t 和 s的交集
c = t – s          # 求差集（项在t中，但不在s中）
d = t ^ s          # 对称差集（项在t或s中，但不会同时出现在二者中）
基本操作：
t.add('x')            # 添加一项
s.update([10,37,42])  # 在s中添加多项
使用remove()可以删除一项：t.remove('H')
len(s)  set 的长度
x in s 测试 x 是否是 s 的成员
x not in s 测试 x 是否不是 s 的成员
s.issubset(t)  s <= t  测试是否 s 中的每一个元素都在 t 中
s.issuperset(t)  s >= t 测试是否 t 中的每一个元素都在 s 中
s.union(t) s | t  返回一个新的 set 包含 s 和 t 中的每一个元素
s.intersection(t) s & t  返回一个新的 set 包含 s 和 t 中的公共元素
s.difference(t) s - t 返回一个新的 set 包含 s 中有但是 t 中没有的元素
s.symmetric_difference(t) s ^ t 返回一个新的 set 包含 s 和 t 中不重复的元素
s.copy() 返回 set “s”的一个浅复制

请注意：union(), intersection(), difference() 和 symmetric_difference() 的非运算符（non-operator，
就是形如 s.union()这样的）版本将会接受任何 iterable 作为参数。相反，它们的运算符版本（operator based counterparts）要求参数必须是 sets。
这样可以避免潜在的错误，如：为了更可读而使用 set('abc') & 'cbs' 来替代 set('abc').intersection('cbs')。
从 2.3.1 版本中做的更改：以前所有参数都必须是 sets。

另外，Set 和 ImmutableSet 两者都支持 set 与 set 之间的比较。两个 sets 在也只有在这种情况下是相等的：
每一个 set 中的元素都是另一个中的元素（二者互为subset）。一个 set 比另一个 set 小，只有在第一个 set 是第二个 set 的 subset 时（是一个 subset，
但是并不相等）。
一个 set 比另一个 set 打，只有在第一个 set 是第二个 set 的 superset 时（是一个 superset，但是并不相等）。
子 set 和相等比较并不产生完整的排序功能。例如：任意两个 sets 都不相等也不互为子 set，因此以下的运算都会返回 False：a<b, a==b, 或者a>b。
因此，sets 不提供 __cmp__ 方法。
因为 sets 只定义了部分排序功能（subset 关系），list.sort() 方法的输出对于 sets 的列表没有定义。


运算符
   运算结果

hash(s)
   返回 s 的 hash 值


下面这个表列出了对于 Set 可用二对于 ImmutableSet 不可用的运算：

运算符（voperator） 等价于  运算结果

s.update(t)      s |= t 返回增加了 set “t”中元素后的 set “s”

s.intersection_update(t)  s &= t  返回只保留含有 set “t”中元素的 set “s”

s.difference_update(t)  s -= t     返回删除了 set “t”中含有的元素后的 set “s”

s.symmetric_difference_update(t) s ^= t   返回含有 set “t”或者 set “s”中有而不是两者都有的元素的 set “s”

s.add(x) 向 set “s”中增加元素 x

s.remove(x) 从 set “s”中删除元素 x, 如果不存在则引发 KeyError

s.discard(x)  如果在 set “s”中存在元素 x, 则删除

s.pop() 删除并且返回 set “s”中的一个不确定的元素, 如果为空则引发 KeyError

s.clear() 删除 set “s”中的所有元素


请注意：非运算符版本的 update(), intersection_update(), difference_update()和symmetric_difference_update()将会接受任意 iterable 作为参数。
从 2.3.1 版本做的更改：以前所有参数都必须是 sets。

还请注意：这个模块还包含一个 union_update() 方法，它是 update() 方法的一个别名。包含这个方法是为了向后兼容。
程序员们应该多使用 update() 方法，因为这个方法也被内置的 set() 和 frozenset() 类型支持。




生成器

range不是生成器 和 xrange 是生成器

readlines不是生成器 和 xreadlines 是生成器

生成器内部基于yield创建，即：对于生成器只有使用时才创建，从而不避免内存浪费


深浅copy
为什么要拷贝？ 当进行修改时，想要保留原来的数据和修改后的数据

数字字符串 和 集合 在修改时的差异？（深浅拷贝不同的终极原因）

在修改数据时：
  数字字符串：在内存中新建一份数据
         集合：修改内存中的同一份数据

对于集合，如何保留其修改前和修改后的数据？ 在内存中拷贝一份
对于集合，如何拷贝其n层元素同时拷贝？ 深拷贝

'''
浅copy
>>> dict = {"a":("apple",),"bo":{"b":"banna","o":"orange"},"g":["grape","grapefruit"]}
>>> dict = {"a":("apple",),"bo":{"b":"banna","o":"orange"},"g":["grape","grapefruit"]}
>>> dict2 = dict.copy()


>>> dict["g"][0] = "shuaige"  #第一次我修改的是第二层的数据
>>> print dict
{'a': ('apple',), 'bo': {'b': 'banna', 'o': 'orange'}, 'g': ['shuaige', 'grapefruit']}
>>> print dict2
{'a': ('apple',), 'bo': {'b': 'banna', 'o': 'orange'}, 'g': ['shuaige', 'grapefruit']}
>>> id(dict["g"][0]),id(dict2["g"][0])
(140422980581296, 140422980581296)  #从这里可以看出第二层他们是用的内存地址
>>>


>>> dict["a"] = "dashuaige"  #注意第二次这里修改的是第一层
>>> print dict
{'a': 'dashuaige', 'bo': {'b': 'banna', 'o': 'orange'}, 'g': ['shuaige', 'grapefruit']}
>>> print dict2
{'a': ('apple',), 'bo': {'b': 'banna', 'o': 'orange'}, 'g': ['shuaige', 'grapefruit']}
>>>
>>> id(dict["a"]),id(dict2["a"])
(140422980580816, 140422980552272)  #从这里看到第一层他们修改后就不会是相同的内存地址了！
>>>


#这里看下，第一次我修改了dict的第二层的数据，dict2也跟着改变了，但是我第二次我修改了dict第一层的数据dict2没有修改。
说明：浅copy只是第一层是独立的，其他层面是公用的！作用节省内存

深copy

#!/usr/bin/env python
#coding:utf-8
import copy  #深copy需要导入模块
dict = {"a":("apple",),"b":{"b":"banna","c":"orange"},"d":["aaa","bat"]}
dict2 = copy.deepcopy(dict)
print "dict:",dict
print "dict2",dict2
dict["d"][0] = "fly"   #修改第二层数据
print "dict2:", dict2
print "dict:",dict
print "id dict:", id(dict["d"][0])
print  "id dict2",id(dict2["d"][0])


'''
dict: {'a': ('apple',), 'b': {'c': 'orange', 'b': 'banna'}, 'd': ['aaa', 'bat']}
dict2 {'a': ('apple',), 'b': {'c': 'orange', 'b': 'banna'}, 'd': ['aaa', 'bat']}
dict2: {'a': ('apple',), 'b': {'c': 'orange', 'b': 'banna'}, 'd': ['aaa', 'bat']}
dict: {'a': ('apple',), 'b': {'c': 'orange', 'b': 'banna'}, 'd': ['fly', 'bat']}
id dict: 38856944
id dict2 38856744
'''
  #从这里看到第二个数据现在也不是公用了

# 通过这里可以看出他们现在是一个完全独立的，当你修改dict时dict2是不会改变的因为是两个独立的字典！

'''





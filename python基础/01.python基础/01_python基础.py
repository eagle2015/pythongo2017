为什么要学编程

传统运维(测试，技术支持)现状

一般运维做两三年，会有瓶颈
大公司运维的现状
云的发展，只运维，不会开发，饭碗被抢
容易被开发绑架
开源软件也需要定制性开发


入门学习编程的方法

慢一点 多理解
多练习，记笔记
把编程当作工具，去解决问题，编程是手段，不是目的
碰到问题google baidu
申请github账号，加入开源社区

----------------------
内容简介

变量 语句
python数据类型
四则运算
获取用户的输入
流程控制
循环


----------------------
注释

代码不仅是可执行的，还要可读
代码一行最前面加一个 # 此行内容不会被执行
方便调试和加上代码解释
'''
    #coding=utf-8
    #获取输入的用户名
    x = raw_input('please input you name ')
    # print it
    print x
'''


字符串--用单引号或者双引号包起来

%s占位符，代表一个字符 语法见代码


'''
        x = 'flying'
        y = 'eagle'
        print 'my name is' + x + ' and I am a '+ y
        print 'my name is %s and I am a %s'  %  (x,y)

'''


字符串格式化


            x = 'flying'
            y = 180
            #报错 数字不能和字符串直接想加
            print 'my name is' + x + ' and I am '+ y + ' cm tall'
            # %s 换成%d 占位符 代表一个数字
            print 'my name is %s and I am %d cm tall'  %  (x,y)


and or

A and B，‘且’，A和B都是真的时候，才为真，否则是假
A or B，‘或’，A和B有一个真的时候，就是真，否则是假


流程控制

if else 语句 实现逻辑控制


    if(判断真假):
        如果是真 执行 （缩进）
    else：
        如果是假 执行
    这里的语句，和if无关 都会执行


逻辑控制

多层if判断


            x = raw_input('please enter you name ')
            if x=='flying':
                print 'you are a nice girl!'
            elif x=='eagle':
                print 'you are nice too!'
            else:
                print 'nice to meet you'


逻辑控制

if可以嵌套多层 (多层缩进)


            x = raw_input('please enter you name:')
            y = raw_input('please enter your age: ')
            if x == 'flying':
                if y=='27':
                    print "%s %s is old" %(x,y)
                elif y == '10':
                    print  "%s %s is young" %(x,y)
                else:
                    print 'I don"n know'
            else:
                print 'not an age'


循环--while

一直循环执行语句,注意缩进



            #注意缩进
            while 判断条件:
                #如果判断条件是真，循环体的语句就会一直执行
                语句1
                语句2
                修改判断条件中的变量，使得循环是可以结束的
            这里的语句，和wilie无关（缩进）



循环--while


            i=0
            while i< 100:
                print i
                i = i + 1
[slide]

循环--while


            name = ''
            while not name:
                name = raw_input('please enter you name:')

            print 'hello python '+name


for循环

可以用来遍历一个序列
name = ['flying','eagle','python','go','bat','a','b','t']
for name in  range(0,len(name)):
    print "##"* name,name


break语句，可以跳出循环（for，while）

跳出哪个循环，由代码缩进决定

    name = ['flying', 'eagle', 'python', 'go', 'bat', 'a', 'b', 't']
    for name in range(0, len(name)):
        if num == 7:
            #num大于7的时候，结束整个循环
            break
        print num


#continue  可以跳出当前这一次循环，从下次开始继续循环（for，while）
for num in range(5, 15):
    if num == 9:
        # num等于7的时候，结束当前循环，继续下一次循环，所以8.9还会打印出来
        continue
    print num

字典
一Python 字典Dictionary
二访问字典里的值
三修改字典
四删除字典元素
五删除字典元素
六字典内置函数
一Python 字典Dictionary cmp方法
二Python 字典Dictionary len方法
三Python 字典Dictionary str方法
四Python 字典Dictionary type方法
七字典内置方法
一Python 字典Dictionary clear方法
二Python 字典Dictionary copy方法
三Python 字典Dictionary fromkeys方法
四Python 字典Dictionary get方法
五Python 字典Dictionary has_key方法
六Python 字典Dictionary items方法
七Python 字典Dictionary keys方法
八Python 字典Dictionary setdefault方法
九Python 字典Dictionary update方法
十Python 字典Dictionary values方法

一、Python 字典(Dictionary)
字典是另一种可变容器模型，且可存储任意类型对象，如其他容器模型。

字典由键和对应值成对组成。字典也被称作关联数组或哈希表。基本语法如下：

dict = {'flying': '12341', 'Bat': '91032', 'eagle': '13258'}
也可如此创建字典：

dict1 = {'abc': 45689};
dict2 = {'abc': 99123, 908.6: 37};

每个键与值用冒号隔开（:），每对用逗号，每对用逗号分割，整体放在花括号中（{}）。
键必须独一无二，但值则不必。
值可以取任何数据类型，但必须是不可变的，如字符串，数或元组。

二、访问字典里的值
把相应的键放入熟悉的方括弧，如下实例:


# !/usr/bin/python

dict = {'Name': 'flying', 'Age': 7, 'Class': 'First'};

print "dict['Name']: ", dict['Name'];
print "dict['Age']: ", dict['Age'];
以上实例输出结果：

dict['Name']:  flying
dict['Age']:  7

如果用字典里没有的键访问数据，会输出错误如下：

# !/usr/bin/python

dict = {'Name': 'flying', 'Age': 7, 'Class': 'First'};

print "dict['flying']: ", dict['name'];
print "dict['flying']: ", dict['flying'];

以上实例输出结果：

dict['flying']:  flying
dict['flying']:
Traceback (most recent call last):
  File "C:/Users/admin/PycharmProjects/pythongo2017/pythoncode/dic.py", line 7, in <module>
    print "dict['flying']: ", dict['flying'];
KeyError: 'flying'


三、修改字典
向字典添加新内容的方法是增加新的键 / 值对，修改或删除已有键 / 值对如下实例:

# !/usr/bin/python

dict = {'Name': 'fly', 'Age': 7, 'Class': 'First'};

dict['Age'] = 18;  # update existing entry
dict['School'] = "flying School";  # Add new entry

print "dict['Age']: ", dict['Age'];
print "dict['School']: ", dict['School'];

以上实例输出结果：

dict['Age']:  8
dict['School']:  flying
School

四、删除字典元素
能删单一的元素也能清空字典，清空只需一项操作。
显示删除一个字典用del命令，如下实例：


# !/usr/bin/python

dict = {'Name': 'fly', 'Age': 7, 'Class': 'First'};

del dict['Name'];  # 删除键是'Name'的条目
dict.clear();  # 清空词典所有条目
del dict;  # 删除词典

print "dict['Age']: ", dict['Age'];
print "dict['School']: ", dict['School'];
但这会引发一个异常，因为用del后字典不再存在：


dict['Age']:Traceback(most recent call last):File"test.py", line8, in < module >print "dict['Age']: ", dict['Age'];
TypeError: 'type'object is unsubscriptable


五、删除字典元素
字典键的特性
字典值可以没有限制地取任何Python对象，既可以是标准的对象，也可以是用户定义的，但键不行。
两个重要的点需要记住：
1、不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：

# !/usr/bin/python

dict = {'Name': 'eagle', 'Age': 7, 'Name': 'flying'};

print "dict['Name']: ", dict['Name'];
以上实例输出结果：

dict['Name']:  Manni

2、键必须不可变，所以可以用数，字符串或元组充当，所以用列表就不行，如下实例：

# !/usr/bin/python

dict = {['Name']: 'flying', 'Age': 7};

print "dict['Name']: ", dict['Name'];
输出结果：

   dict = {['Name']: 'flying', 'Age': 7};
TypeError: unhashable type: 'list'


六、字典内置函数
Python字典包含了以下内置函数：
序号      函数及描述
1        cmp(dict1, dict2)   比较两个字典元素。
2        len(dict)           计算字典元素个数，即键的总数。
3        str(dict)           输出字典可打印的字符串表示。
4        type(variable)      返回输入的变量类型，如果变量是字典就返回字典类型。

详细解释：
（一）Python  字典(Dictionary)
cmp() 方法
1、描述 Python 字典(Dictionary) cmp()  函数比较两个字典元素。
2、语法 cmp() 方法语法：
cmp(dict1, dict2)
3、参数
dict1 - - 比较的字典。
dict2 - - 比较的字典。
4、返回值
如果两个字典的元素相同返回0，如果字典dict1大于字典dict2返回1，如果字典dict1小于于字典dict2返回1。
5、实例
以下实例展示了 cmp()函数的使用方法：

# !/usr/bin/python

dict1 = {'Name': 'flying', 'Age': 7};
dict2 = {'Name': 'fly', 'Age': 27};
dict3 = {'Name': 'eagle', 'Age': 27};
dict4 = {'Name': 'bat', 'Age': 7};
print "Return Value : %d" % cmp(dict1, dict2)
print "Return Value : %d" % cmp(dict2, dict3)
print "Return Value : %d" % cmp(dict1, dict4)
以上实例输出结果为：
Return Value : -1
Return Value : 1
Return Value : 1

（二）Pythonc字典(Dictionary) len() 方法
1、描述 Python 字典(Dictionary) len() 函数计算字典元素个数，即键的总数。
2、语法 len() 方法语法： len(dict)
3、参数 dict - - 要计算元素个数的字典。
4、返回值 返回字典的元素个数。
5、实例 以下实例展示了 len()  函数的使用方法：

# !/usr/bin/python

dict = {'Name': 'flying', 'Age': 7};
print "Length : %d" % len(dict)
以上实例输出结果为：

Length: 2

（三）Python 字典(Dictionary) str()方法
1、描述  Python 字典(Dictionary) str() 函数将值转化为适于人阅读的形式，以可打印的字符串表示。
2、语法 str() 方法语法：str(dict)
3、参数 dict - - 字典。
4、返回值 返回字符串。
5、实例 以下实例展示了 str()
函数的使用方法：

# !/usr/bin/python

dict = {'Name': 'flying', 'Age': 7};
print "Equivalent String : %s" % str(dict)
以上实例输出结果为：

Equivalent String : {'Age': 27, 'Name': 'flying'}

（四）Python字典(Dictionary) type() 方法
1、描述Python字典(Dictionary) type() 函数返回输入的变量类型，如果变量是字典就返回字典类型。
2、语法type()方法语法：type(dict)
3、参数 dict - - 字典。
4、返回值返回输入的变量类型。
5、实例
以下实例展示了type() 函数的使用方法：

# !/usr/bin/python

dict = {'Name': 'flying', 'Age': 27};
print "Variable Type : %s" % type(dict)
以上实例输出结果为：

Variable Type: < type'dict' >

七、字典内置方法
Python字典包含了以下内置函数：
序号  函数及描述
1  radiansdict.clear()   删除字典内所有元素
2  radiansdict.copy()    返回一个字典的浅复制
3 radiansdict.fromkeys() 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
4 radiansdict.get(key, default=None) 返回指定键的值，如果值不在字典中返回default值
5 radiansdict.has_key(key)   如果键在字典dict里返回true，否则返回false
6 radiansdict.items()以列表返回可遍历的(键, 值) 元组数组
7 radiansdict.keys() 以列表返回一个字典所有的键
8 radiansdict.setdefault(key, default=None) 和get()类似, 但如果键不已经存在于字典中，将会添加键并将值设为default
9 radiansdict.update(dict2) 把字典dict2的键 / 值对更新到dict里
10 radiansdict.values() 以列表返回字典中的所有值
详细解释：
（一）Python 字典(Dictionary) clear()方法
1、描述Python 字典(Dictionary) clear() 函数用于删除字典内所有元素。
2、语法clear()方法语法： dict.clear()
3、参数 NA
4、返回值 该函数没有任何返回值。
5、实例 以下实例展示了clear() 函数的使用方法：

# !/usr/bin/python

dict = {'Name': 'flying', 'Age': 27,'work':'PE'};

print "Start Len : %d" % len(dict)
dict.clear()
print "End Len : %d" % len(dict)
以上实例输出结果为：

Start Len: 3
End Len: 0

（二）Python 字典(Dictionary) copy() 方法
1、描述 Python 字典(Dictionary) copy() 函数返回一个字典的浅复制。
2、语法
copy()
方法语法：
dict.copy()
3、参数
NA。
4、返回值
返回一个字典的浅复制。
5、实例
以下实例展示了
copy()
函数的使用方法：
[python]
view
plain
copy
print?在CODE上查看代码片派生到我的代码片
# !/usr/bin/python

dict1 = {'Name': 'Zara', 'Age': 7};

dict2 = dict1.copy()
print "New Dictinary : %s" % str(dict2)
以上实例输出结果为:
[python]
view
plain
copy
print?在CODE上查看代码片派生到我的代码片
New
Dictinary: {'Age': 7, 'Name': 'Zara'}

（三）Python
字典(Dictionary)
fromkeys()
方法
1、描述
Python
字典(Dictionary)
fromkeys()
函数用于创建一个新字典，以序列seq中元素做字典的键，value为字典所有键对应的初始值。
2、语法
fromkeys()
方法语法：
[python]
view
plain
copy
print?在CODE上查看代码片派生到我的代码片
dict.fromkeys(seq[, value]))
3、参数
seq - - 字典键值列表。
value - - 可选参数, 设置键序列（seq）的值。
4、返回值
该方法返回列表。
5、实例
以下实例展示了
fromkeys()
函数的使用方法：
[python]
view
plain
copy
print?在CODE上查看代码片派生到我的代码片
# !/usr/bin/python

seq = ('name', 'age', 'sex')

dict = dict.fromkeys(seq)
print "New Dictionary : %s" % str(dict)

dict = dict.fromkeys(seq, 10)
print "New Dictionary : %s" % str(dict)
以上实例输出结果为：
[python]
view
plain
copy
print?在CODE上查看代码片派生到我的代码片
New
Dictionary: {'age': None, 'name': None, 'sex': None}
New
Dictionary: {'age': 10, 'name': 10, 'sex': 10}

（四）Python
字典(Dictionary)
get()
方法
1、描述
Python
字典(Dictionary)
get()
函数返回指定键的值，如果值不在字典中返回默认值。
2、语法
get()
方法语法：
[python]
view
plain
copy
print?在CODE上查看代码片派生到我的代码片
dict.get(key, default=None)
3、参数
key - - 字典中要查找的键。
default - - 如果指定键的值不存在时，返回该默认值值。
4、返回值
返回指定键的值，如果值不在字典中返回默认值None。
5、实例
以下实例展示了
get()
函数的使用方法：
[python]
view
plain
copy
print?在CODE上查看代码片派生到我的代码片
# !/usr/bin/python

dict = {'Name': 'Zara', 'Age': 27}

print "Value : %s" % dict.get('Age')
print "Value : %s" % dict.get('Sex', "Never")
以上实例输出结果为：
[python]
view
plain
copy
print?在CODE上查看代码片派生到我的代码片
Value: 27
Value: Never

（五）Python
字典(Dictionary)
has_key()
方法
1、描述
Python
字典(Dictionary)
has_key()
函数用于判断键是否存在于字典中，如果键在字典dict里返回true，否则返回false。
2、语法
has_key()
方法语法：
[python]
view
plain
copy
print?在CODE上查看代码片派生到我的代码片
dict.has_key(key)
3、参数
key - - 要在字典中查找的键。
4、返回值
如果键在字典里返回true，否则返回false。
5、实例
以下实例展示了
has_key()
函数的使用方法：
[python]
view
plain
copy
print?在CODE上查看代码片派生到我的代码片
# !/usr/bin/python

dict = {'Name': 'Zara', 'Age': 7}

print "Value : %s" % dict.has_key('Age')
print "Value : %s" % dict.has_key('Sex')
以上实例输出结果为：
[python]
view
plain
copy
print?在CODE上查看代码片派生到我的代码片
Value: True
Value: False

（六）Python
字典(Dictionary)
items()
方法
1、描述
Python
字典(Dictionary)
items()
函数以列表返回可遍历的(键, 值)
元组数组。
2、语法
items()
方法语法：
[python]
view
plain
copy
print?在CODE上查看代码片派生到我的代码片
dict.items()
3、参数
NA。
4、返回值
返回可遍历的(键, 值)
元组数组。
5、实例
以下实例展示了
items()
函数的使用方法：
[python]
view
plain
copy
print?在CODE上查看代码片派生到我的代码片
# !/usr/bin/python

dict = {'Name': 'Zara', 'Age': 7}

print "Value : %s" % dict.items()
以上实例输出结果为：
[python]
view
plain
copy
print?在CODE上查看代码片派生到我的代码片
Value: [('Age', 7), ('Name', 'Zara')]

（七）Python
字典(Dictionary)
keys()
方法
1、描述
Python
字典(Dictionary)
keys()
函数以列表返回一个字典所有的键。
2、语法
keys()
方法语法：
[python]
view
plain
copy
print?在CODE上查看代码片派生到我的代码片
dict.keys()
3、参数
NA。
4、返回值
返回一个字典所有的键。
5、实例
以下实例展示了
keys()
函数的使用方法：
[python]
view
plain
copy
print?在CODE上查看代码片派生到我的代码片
# !/usr/bin/python

dict = {'Name': 'Zara', 'Age': 7}

print "Value : %s" % dict.keys()
以上实例输出结果为：
[python]
view
plain
copy
print?在CODE上查看代码片派生到我的代码片
Value: ['Age', 'Name']

（八）Python
字典(Dictionary)
setdefault()
方法
1、描述
Python
字典(Dictionary)
setdefault()
函数和get()
方法类似, 如果键不已经存在于字典中，将会添加键并将值设为默认值。
2、语法
setdefault()
方法语法：
[python]
view
plain
copy
print?在CODE上查看代码片派生到我的代码片
dict.setdefault(key, default=None)
3、参数
key - - 查找的键值。
default - - 键不存在时，设置的默认键值。
4、返回值
该方法没有任何返回值。
5、实例
以下实例展示了
setdefault()
函数的使用方法：
[python]
view
plain
copy
print?在CODE上查看代码片派生到我的代码片
# !/usr/bin/python

dict = {'Name': 'Zara', 'Age': 7}

print "Value : %s" % dict.setdefault('Age', None)
print "Value : %s" % dict.setdefault('Sex', None)
以上实例输出结果为：
[python]
view
plain
copy
print?在CODE上查看代码片派生到我的代码片
Value: 7
Value: None

（九）Python
字典(Dictionary)
update()
方法
1、描述
Python
字典(Dictionary)
update()
函数把字典dict2的键 / 值对更新到dict里。
2、语法
update()
方法语法：
[python]
view
plain
copy
print?在CODE上查看代码片派生到我的代码片
dict.update(dict2)
3、参数
dict2 - - 添加到指定字典dict里的字典。
4、返回值
该方法没有任何返回值。
5、实例
以下实例展示了
update()
函数的使用方法：
[python]
view
plain
copy
print?在CODE上查看代码片派生到我的代码片
# !/usr/bin/python

dict = {'Name': 'Zara', 'Age': 7}
dict2 = {'Sex': 'female'}

dict.update(dict2)
print "Value : %s" % dict
以上实例输出结果为：
[python]
view
plain
copy
print?在CODE上查看代码片派生到我的代码片
Value: {'Age': 7, 'Name': 'Zara', 'Sex': 'female'}


（十）Python
字典(Dictionary)
values()
方法
1、描述
Python
字典(Dictionary)
values()
函数以列表返回字典中的所有值。
2、语法
values()
方法语法：
[python]
view
plain
copy
print?在CODE上查看代码片派生到我的代码片
dict.values()
3、参数
NA。
4、返回值
返回字典中的所有值。
5、实例
以下实例展示了
values()
函数的使用方法：
[python]
view
plain
copy
print?在CODE上查看代码片派生到我的代码片
# !/usr/bin/python

dict = {'Name': 'Zara', 'Age': 7}

print "Value : %s" % dict.values()
以上实例输出结果为：
[python]
view
plain
copy
print?在CODE上查看代码片派生到我的代码片
Value: [7, 'Zara']

        ---------------------------------------------
dict 就是key value值，索引有意义

和list的区别

# 定义dict
d = {
'name':'flying'
}
# 获取dict值
print d['name']

# 增加新值
d['age'] = 22
print d['age']
# 修改值

d['name'] = 'eagle'
print d['name']
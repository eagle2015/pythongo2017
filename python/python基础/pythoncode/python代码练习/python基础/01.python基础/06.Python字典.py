Python字典
字典(dictionary)是除列表意外python之中最灵活的内置数据结构类型。列表是有序的对象结合，字典是无序的对象集合。
1、字典与列表的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
2、字典用"{ }"标识。字典由索引(key)和它对应的值value组成。


dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict  =  {'age': 27, 'Work': 'PE', 'Name': 'fly', 'Sex': 'female'}

print dict['one']  # 输出键为'one' 的值
print dict[2]  # 输出键为 2 的值
print tinydict  # 输出完整的字典
print tinydict.keys()  # 输出所有键
print tinydict.values()  # 输出所有值

'''
This is one
This is two
{'age': 27, 'Work': 'PE', 'Name': 'fly', 'Sex': 'female'}
['age', 'Work', 'Name', 'Sex']
[27, 'PE', 'fly', 'female']
'''

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


Python 字典可以使用键作为索引来访问/更新/添加值

info = dict()
info['name'] = 'flying'
info['Age'] = '27'
info['Work'] = 'PE'
print info

------------
>>> info = dict()
>>> info['name'] = 'flying'
>>> print info
{'name': 'flying'}
>>> info['Age'] = '27'
>>> info['Work'] = 'PE'
>>> print info
{'Age': '27', 'Work': 'PE', 'name': 'flying'}
>>> info
{'Age': '27', 'Work': 'PE', 'name': 'flying'}
>>>
----------------

# !/usr/bin/python

dict = {'Name': 'flying', 'Age': 27, 'Class': 'First'};

print "dict['Name']: ", dict['Name'];
print "dict['Age']: ", dict['Age'];
以上实例输出结果：

dict['Name']:  flying
dict['Age']:  27

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
2、语法copy() 方法语法：dict.copy()
3、参数NA。
4、返回值返回一个字典的浅复制。
5、实例以下实例展示了copy()函数的使用方法：

# !/usr/bin/python

dict1 = {'Name': 'flying', 'Age': 27,'work':'PE'};
dict2 = dict1.copy()
print "New Dictinary : %s" % str(dict2)


以上实例输出结果为:

New Dictinary : {'Age': 27, 'work': 'PE', 'Name': 'flying'}

（三）Python字典(Dictionary) fromkeys()方法
1、描述 Python字典(Dictionary)  fromkeys()函数用于创建一个新字典，以序列seq中元素做字典的键，value为字典所有键对应的初始值。
2、语法 fromkeys() 方法语法：dict.fromkeys(seq[, value]))
3、参数
seq - - 字典键值列表。
value - - 可选参数, 设置键序列（seq）的值。
4、返回值 :该方法返回列表。
5、实例
以下实例展示了 fromkeys() 函数的使用方法：

# !/usr/bin/python

seq = ('name', 'age', 'sex','work')

dict = dict.fromkeys(seq)
print "New Dictionary : %s" % str(dict)

dict = dict.fromkeys(seq, 10)
print "New Dictionary : %s" % str(dict)
以上实例输出结果为：



'''
结果：
New Dictionary : {'age': None, 'work': None, 'name': None, 'sex': None}
New Dictionary : {'age': 10, 'work': 10, 'name': 10, 'sex': 10}
'''

（四）Python 字典(Dictionary)  get()方法
1、描述Python字典(Dictionary) get()函数返回指定键的值，如果值不在字典中返回默认值。
2、语法 get()方法语法：dict.get(key, default=None)
3、参数
key - - 字典中要查找的键。
default - - 如果指定键的值不存在时，返回该默认值值。
4、返回值:返回指定键的值，如果值不在字典中返回默认值None。
5、实例
get()函数的使用方法：

# !/usr/bin/python

dict = {'Name': 'flying', 'Age': 27,'work':'PE'}

dict = {'Name': 'flying', 'Age': 27,'Work':'PE'};
print "Age Value : %s" % dict.get('Age')
print "Sex Value : %s" % dict.get('Sex', "Never")
print "Work Value : %s" % dict.get('Work')
print "Name Value : %s" % dict.get('Name')

以上实例输出结果为：

Age Value : 27
Sex Value : Never
Work Value : PE
Name Value : flying


（五）Python 字典(Dictionary) has_key()方法
1、描述Python字典(Dictionary):  has_key() 函数用于判断键是否存在于字典中，如果键在字典dict里返回true，否则返回false。
2、语法:has_key()方法语法：dict.has_key(key)
3、参数:key - - 要在字典中查找的键。
4、返回值:如果键在字典里返回true，否则返回false。
5、实例:has_key()函数的使用方法：

# !/usr/bin/python

dict = {'Name': 'flying', 'Age': 27,'Work':'PE'};
print "Age Value : %s" % dict.has_key('Age')
print "Sex Value : %s" % dict.has_key('Sex')
print "Work Value : %s" % dict.has_key('Work')
print "Name Value : %s" % dict.has_key('Name')

以上实例输出结果为：
Age Value : True
Sex Value : False
Work Value : True
Name Value : True



（六）Python字典(Dictionary)items()方法
1、描述:Python字典(Dictionary) items()函数以列表返回可遍历的(键, 值)元组数组。
2、语法:items()方法语法：dict.items()
3、参数:NA。
4、返回值:返回可遍历的(键, 值)元组数组。
5、实例:items()函数的使用方法：

# !/usr/bin/python

dict = {'Name': 'flying', 'Age': 27,'Work':'PE'};

print "Value : %s" % dict.items()
以上实例输出结果为：
Value : [('Age', 27), ('Work', 'PE'), ('Name', 'flying')]


（七）Python字典(Dictionary) keys()方法
1、描述 :Python字典(Dictionary)keys() 函数以列表返回一个字典所有的键。
2、语法:keys()方法语法：dict.keys()
3、参数NA。
4、返回值:返回一个字典所有的键。
5、实例:keys()函数的使用方法：

# !/usr/bin/python


dict = {'Name': 'flying', 'Age': 27,'Work':'PE'};
print "Value : %s" % dict.keys()
输出结果为：
Value: ['Age', 'Work', 'Name']


（八）Python字典(Dictionary)setdefault()方法
1、描述:Python字典(Dictionary) setdefault()函数和get()方法类似, 如果键不已经存在于字典中，将会添加键并将值设为默认值。
2、语法:
        setdefault() 方法语法：dict.setdefault(key, default=None)
3、参数:
key - - 查找的键值。
default - - 键不存在时，设置的默认键值。
4、返回值:该方法没有任何返回值。
5、实例:setdefault()
函数的使用方法：

# !/usr/bin/python

dict = {'Name': 'flying', 'Age': 27,'Work':'PE'};

print "Value : %s" % dict.setdefault('Age', None)
print "Value : %s" % dict.setdefault('Sex', None)
print "Work Value: %s" % dict.setdefault('Name')

输出结果为：
Age Value : 27
Sex Value : None
Work Value: flying


（九）Python 字典(Dictionary) update()方法
1、描述: Python 字典(Dictionary)  update()函数把字典dict2的键值对更新到dict里。
2、语法:
update() 方法语法：dict.update(dict2)
3、参数:dict2 - - 添加到指定字典dict里的字典。
4、返回值:该方法没有任何返回值。
5、实例: update()函数的使用方法：

# !/usr/bin/python

dict = {'Name': 'fly, 'Age': 27}
dict2 = {'Sex': 'female','Work':'PE'}

dict.update(dict2)
print "dict Value : %s" % dict

输出结果为：
dict Value : {'age': 27, 'Work': 'PE', 'Name': 'fly', 'Sex': 'female'}


（十）Python 字典(Dictionary) values() 方法
1、描述: Python 字典(Dictionary) values() 函数以列表返回字典中的所有值。
2、语法:
values() 方法语法：dict.values()
3、参数:NA。
4、返回值:返回字典中的所有值。
5、实例:values()函数的使用方法：

# !/usr/bin/python

dict = {'Name': 'flying', 'Age': 27,'Work':'PE'};

print "values Value : %s" % dict.values()
输出结果为：
values Value : [27, 'PE', 'fly', 'female']


遍历python字典

# 遍历函数
dict = {'age': 27, 'Work': 'PE', 'Name': 'fly', 'Sex': 'female'}
print "#" * 7, "dict", "#" * 7
for key in dict:
    print "dict[%s]:" % key, dict[key]

'''
####### dict #######
dict[age]: 27
dict[Work]: PE
dict[Name]: fly
dict[Sex]: female
'''
print "#" * 10, "iteritems", "#" * 10
for k, v in dict.iteritems():
    print "dict[%s]:" % k, v

print "#" * 15, "items", "$" * 15
for (k, v) in dict.items():
    print "dict[%s]:" % k, v

print "###########iterkeys,itervalues#######"
for k, v in zip(dict.iterkeys(), dict.itervalues()):
    print "dict[%s]=" % k, v

'''
########## iteritems ##########
dict[age]: 27
dict[Work]: PE
dict[Name]: fly
dict[Sex]: female
############### items $$$$$$$$$$$$$$$
dict[age]: 27
dict[Work]: PE
dict[Name]: fly
dict[Sex]: female
###########iterkeys,itervalues#######
dict[age]= 27
dict[Work]= PE
dict[Name]= fly
dict[Sex]= female

'''

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict  =  {'age': 27, 'Work': 'PE', 'Name': 'fly', 'Sex': 'female'}

print dict['one']  # 输出键为'one' 的值
print dict[2]  # 输出键为 2 的值
print tinydict  # 输出完整的字典
print tinydict.keys()  # 输出所有键
print tinydict.values()  # 输出所有值


===================================================================

#最好的是用下面的方法来动态的扩展字典：
a=[111,222,133,414,551,663,737,838,929,920]
dict1={}  #动态的增加字典


'''
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

dict1: {'k2': [111, 222, 133, 414, 551], 'k1': [663, 737, 838, 929, 920]}






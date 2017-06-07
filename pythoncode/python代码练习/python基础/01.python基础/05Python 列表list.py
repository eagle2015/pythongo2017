一 Python 列表
二访问列表中的值
三更新列表
四删除列表元素
五Python列表脚本操作符
六Python列表截取
七Python列表函数
一Python List cmp方法
二Python List len方法
三Python List max方法
四Python List min方法
五Python List list方法
八Python列表方法
一Python List append方法
二Python List count方法
三Python List extend方法
四Python List insert方法
五Python List insert方法
六Python List pop方法
七Python List remove方法
八Python List reverse方法
九Python List sort方法


一、Python 列表
    序列是Python中最基本的数据结构。序列中的每个元素都分配一个数字 - 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推。
    Python有6个序列的内置类型，但最常见的是列表和元组。
    序列都可以进行的操作包括索引，切片，加，乘，检查成员。
    此外，Python已经内置确定序列的长度以及确定最大和最小的元素的方法。
    列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。列表的数据项不需要具有相同的类型。

创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。如下所示：

aList = [123, 'eagle', 'flying', 'bat'];

三、更新列表
你可以对列表的数据项进行修改或更新，你也可以使用append()方法来添加列表项，如下所示

aList = [123, 'eagle', 'flying', 'bat'];
list = [123, 'eagle', 'flying', 'bat']
print "Value available at index 0 : "
print "list[0]:", list[0];
list[0] = 2001;
print "New value available at index 0 : "
print "list[0]:",list[0];
aList.append(2017)
print "aList:",aList

=================================================
Value available at index 0 :
list[0]: 123
New value available at index 0 :
list[0]: 2001
aList: [123, 'eagle', 'flying', 'bat', 2017]


四、删除列表元素
可以使用 del 语句来删除列表的的元素，如下实例：

list = [123, 'eagle', 'flying', 'bat']
list.append(2018)
list.append(2016)
list.append(2017)
list[0]= 2019
print "list:",list
del list[3]
print "new list:",list


list: [2019, 'eagle', 'flying', 'bat', 2016, 2017]
new list: [2019, 'eagle', 'flying', 2016, 2017]


五、Python列表脚本操作符
列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表。
如下所示：

Python 表达式	结果	描述
len([1, 2, 3])	3	                        长度
[1, 2, 3] + [4, 5, 6]	[1, 2, 3, 4, 5, 6]	组合
['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	重复
3 in [1, 2, 3]	True	                    元素是否存在于列表中
for x in [1, 2, 3]: print x,	1 2 3	    迭代


Python遍历列表的四种方法:

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


============================
aList: 123
aList: eagle
aList: flying
aList: bat
1 app_list: 2019
1 app_list: eagle
1 app_list: flying
1 app_list: bat
1 app_list: 2016
1 app_list: 2017
2 app_list[0]  2019
2 app_list[1]  eagle
2 app_list[2]  flying
2 app_list[3]  bat
2 app_list[4]  2016
2 app_list[5]  2017
3 app_list[0]:  2019
3 app_list[1]:  eagle
3 app_list[2]:  flying
3 app_list[3]:  bat
3 app_list[4]:  2016
3 app_list[5]:  2017
4 app_list: 2019
4 app_list: eagle
4 app_list: flying
4 app_list: bat
4 app_list: 2016
4 app_list: 2017


Python列表截取
Python的列表截取与字符串操作类型，如下所示：


Python 表达式	结果	描述
L[2]		读取列表中第三个元素
L[-2]		读取列表中倒数第二个元素
L[1:]		从第二个元素开始截取列表


Python列表函数&方法

Python包含以下函数:
序号	函数
1	cmp(list1, list2) 比较两个列表的元素
2	len(list) 列表元素个数
3	max(list) 返回列表元素最大值
4	min(list) 返回列表元素最小值
5	list(seq) 将元组转换为列表

Python包含以下方法:
序号	方法
1	list.append(obj) 在列表末尾添加新的对象
2	list.count(obj) 统计某个元素在列表中出现的次数
3	list.extend(seq) 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
4	list.index(obj) 从列表中找出某个值第一个匹配项的索引位置
5	list.insert(index, obj) 将对象插入列表
6	list.pop(obj=list[-1]) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
7	list.remove(obj) 移除列表中某个值的第一个匹配项
8	list.reverse() 反向列表中元素
9	list.sort([func]) 对原列表进行排序



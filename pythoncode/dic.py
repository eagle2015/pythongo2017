# !/usr/bin/python
#coding:utf-8

'''
dict = {'Name': 'flying', 'Age': 7, 'Class': 'First'};

print "dict['flying']: ", dict['Name'];

#print "dict['flying']: ", dict['flying'];



dict = {'Name': 'fly', 'Age': 7, 'Class': 'First'};

dict['Age'] = 18;  # update existing entry
dict['School'] = "flying School";  # Add new entry

print "dict['Age']: ", dict['Age'];
print "dict['School']: ", dict['School'];


dict = {'Name': 'fly', 'Age': 7, 'Class': 'First'};

del dict['Name']; # 删除键是'Name'的条目
print dict
#dict.clear();  # 清空词典所有条目
#del dict;  # 删除词典

print "dict['Age']: ", dict['Age'];
#print "dict['School']: ", dict['School'];
#但这会引发一个异常，因为用del后字典不再存在：
'''
'''
#不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：
dict = {'Name': 'eagle', 'Age': 7, 'Name': 'flying'};

print "dict['Name']: ", dict['Name'];
'''

'''
#键必须不可变，所以可以用数，字符串或元组充当，所以用列表就不行，如下实例：
dict = {['Name']: 'flying', 'Age': 7};

print "dict['Name']: ", dict['Name'];

'''

#cmp 如果两个字典的元素相同返回0，如果字典dict1大于字典dict2返回1，如果字典dict1小于于字典dict2返回1。
dict1 = {'Name': 'flying', 'Age': 7};
dict2 = {'Name': 'fly', 'Age': 27};
dict3 = {'Name': 'eagle', 'Age': 27};
dict4 = {'Name': 'bat', 'Age': 7};
print "Return Value : %d" % cmp(dict1, dict2)
print "Return Value : %d" % cmp(dict2, dict3)
print "Return Value : %d" % cmp(dict1, dict4)


dict = {'Name': 'flying', 'Age': 27};
print "Length : %d" % len(dict)
print "Equivalent String : %s" % str(dict)
print "Variable Type : %s" % type(dict)

dict = {'Name': 'flying', 'Age': 27,'work':'PE'};
print "Start Len : %d" % len(dict)
dict.clear()
print "End Len : %d" % len(dict)

'''
Return Value : -1
Return Value : 1
Return Value : 1
Length : 2
Equivalent String : {'Age': 27, 'Name': 'flying'}
Variable Type : <type 'dict'>
Start Len : 3
End Len : 0


# copy() 函数返回一个字典的浅复制。
'''

dict1 = {'Name': 'flying', 'Age': 27,'work':'PE'};
dict2 = dict1.copy()
print "New Dictinary : %s" % str(dict2)
'''

结果：
New Dictinary : {'Age': 27, 'work': 'PE', 'Name': 'flying'}
'''

#fromkeys()函数用于创建一个新字典，以序列seq中元素做字典的键，value为字典所有键对应的初始值。
seq = ('name', 'age', 'sex','work')

dict = dict.fromkeys(seq)
print "New Dictionary : %s" % str(dict)

dict = dict.fromkeys(seq, 10)
print "New Dictionary : %s" % str(dict)

'''
结果：
New Dictionary : {'age': None, 'work': None, 'name': None, 'sex': None}
New Dictionary : {'age': 10, 'work': 10, 'name': 10, 'sex': 10}
'''
#get()返回指定键的值，如果值不在字典中返回默认值None。
dict = {'Name': 'flying', 'Age': 27,'Work':'PE'};
print "Age Value : %s" % dict.get('Age')
print "Sex Value : %s" % dict.get('Sex', "Never")
print "Work Value : %s" % dict.get('Work')
print "Name Value : %s" % dict.get('Name')

#has_key()如果键在字典里返回true，否则返回false。
print "Age Value : %s" % dict.has_key('Age')
print "Sex Value : %s" % dict.has_key('Sex')
print "Work Value : %s" % dict.has_key('Work')
print "Name Value : %s" % dict.has_key('Name')

print "Value : %s" % dict.items()

'''
Value : [('Age', 27), ('Work', 'PE'), ('Name', 'flying')]
'''

#keys返回一个字典所有的键。
print "Value: %s " % dict.keys()
'''
Value: ['Age', 'Work', 'Name']
'''

# setdefault()函数和get()方法类似, 如果键不已经存在于字典中，将会添加键并将值设为默认值。
print "Age Value : %s" % dict.setdefault('Age', None)
print "Sex Value : %s" % dict.setdefault('Sex', None)
print "Work Value: %s" % dict.setdefault('Name')

'''
结果：
Age Value : 27
Sex Value : None
Work Value: flying
'''

dict = {'Name': 'fly', 'age': 27}
dict2 = {'Sex': 'female','Work':'PE'}

dict.update(dict2)
print "dict Value : %s" % dict

'''
dict Value : {'age': 27, 'Work': 'PE', 'Name': 'fly', 'Sex': 'female'}
'''

#values() 函数以列表返回字典中的所有值。
print "value Value : %s" % dict.values()
#keys返回一个字典所有的键。
print "keys Value: %s " % dict.keys()

value Value : [27, 'PE', 'fly', 'female']
keys Value: ['age', 'Work', 'Name', 'Sex']
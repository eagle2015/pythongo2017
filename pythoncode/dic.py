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


dict = {'Name': 'flying', 'Age': 7};
print "Length : %d" % len(dict)
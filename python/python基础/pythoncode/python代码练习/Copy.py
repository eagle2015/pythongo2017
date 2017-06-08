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

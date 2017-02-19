Python基础知识
一 Python简介
什么是Python
Python的设计理念
Python的标准库
Python常见的开发环境
Python常见的解释器

二 Python程序的基本架构
三 Python的输入和输出语句
 1 Python的输出语句
    print简单输出
    print格式化输出
 2 Python的输入语句

一、Python简介
1、什么是Python
    Python是一种解释型、面向对象、动态数据类型的高级程序设计语言。自从20世纪90年代初Python语言诞生至今，它逐渐被广泛应用于处理系统管理任务和Web编程。Python是完全面向对象的语言。函数、模块、数字、字符串都是对象。并且完全支持继承、重载、派生、多继承，有益于增强源代码的复用性。Python支持重载运算符和动态类型。
2、Python的设计理念
    Python的设计哲学是“优雅”、“明确”、“简单”。因此，Perl语言中“总是有多种方法来做同一件事”的理念在Python开发者中通常是难以忍受的。Python开发者的哲学是“用一种方法，最好是只有一种方法来做一件事”。
3、Python的标准库
    Python拥有一个强大的标准库。Python语言的核心只包含数字、字符串、列表、字典、文件等常见类型和函数，而由Python标准库提供了系统管理、网络通信、文本处理、数据库接口、图形系统、XML处理等额外的功能。Python标准库命名接口清晰、文档良好，很容易学习和使用。
    Python标准库的主要功能有：
（1）文本处理
包含文本格式化、正则表达式匹配、文本差异计算与合并、Unicode支持，二进制数据处理等功能
（2）文件处理
包含文件操作、创建临时文件、文件压缩与归档、操作配置文件等功能
（3）操作系统功能
包含线程与进程支持、IO复用、日期与时间处理、调用系统函数、写日记(logging)等功能
（4）网络通信
包含网络套接字，SSL加密通信、异步网络通信等功能
（5）网络协议
支持HTTP，FTP，SMTP，POP，IMAP，NNTP，XMLRPC等多种网络协议，并提供了编写网络服务器的框架
（6）W3C格式支持
包含HTML，SGML，XML的处理。
（7）其它功能
包括国际化支持、数学运算、HASH、Tkinter等
4、Python常见的开发环境
（1）IDLE：Python内置IDE (随python安装包提供)
（2）PyCharm[6]：详见百度百科PyCharm，由著名的JetBrains公司开发，带有一整套可以帮助用户在使用Python语言开发时提高其效率的工 具，比如调试、语法高亮、Project管理、代码跳转、智能提示、自动完成、单元测试、版本控制。此外，该IDE提供了一些高级功能，以用于支持Django框架下的专业Web开发。
（3）PythonWin：ActivePython或pywin32均提供该IDE，仅适用于Windows
（4）PyPE：一个开源的跨平台的PythonIDE。
（5）eclipse + pydev插件：方便调试程序
（6）emacs：自带python支持，自动补全、refactor等功能需要插件支持
（7）Vim: 最新7.3版编译时可以加入python支持，提供python代码自动提示支持
（8）Visual Studio 2010 + Python Tools for Visual Studio
（9）TextMate
（10）Netbeans IDE
    另外，诸如EditPlus、UltraEdit等通用的程序员文本编辑器软件也能对Python代码编辑提供一定的支持，比如代码自动着色、注释快捷键等，但是否够得上集成开发环境的水平，尚有待评估。
5、Python常见的解释器
（1）Python
    是一门跨平台的脚本语言，Python规定了一个Python语法规则，实现了Python语法的解释程序就成为了Python的解释器。
（2）CPython
   ClassicPython，也就是原始的Python实现，需要区别于其他实现的时候才以CPython称呼；或解作C语言实现的Python。这是最常用的Python版本。
（3）Jython
   原名JPython；Java语言实现的Python，现已正式发布。Jython可以直接调用Java的各种函数库。
（4）PyPy
   使用Python语言写的Python。

二、Python程序的基本架构
Python跟其他的编程语言一样，基本架构都如下图所示：

输入 ==========》处理=============》输出


说明：
1、输入方式有变量赋值和输入语句两种（当然不局限这两种）；
2、处理方式有算术运算、逻辑运算和算法处理；
3、输出方式有打印输出，写入文件和写入数据库（后面两种输出方式后面再介绍）。


eg1：
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
上述例子的执行过程是：输入（变量赋值）->处理（算术运算）->输出（打印输出）

eg2：
>>> str1=raw_input("Please input your name: ")
Please input your name: flying
>>> print (str1)
flying

上述例子的执行过程是：输入（输入语句）->处理（逻辑运算）->输出（打印输出）

三、Python的输入和输出语句
（一）Python的输出语句
1、print()简单输出


2、print()格式化输出
（1）格式
     print(format(value,format_modifier)) 即   print(format(value,'m,nf'))
（2）说明：
value：数值
format_modifier：格式字
m：输出占位符
n：精度

>>> print (format(12.3456,'6.2f'))
 12.35
>>> print (format(12.3456,'6.9f'))
12.345600000
>>> print (format(12.3456,'9.2f'))
    12.35
>>> print (format(12.3456,'3.2f'))
12.35
>>> print (format(0.3456,'.2%'))
34.56%
>>> print (format(0.3456,'3.2%'))
34.56%
>>> print (format(0.3456,'1.3%'))
34.560%

（二）Python的输入语句
Python输入语句主要采用raw_input函数

从raw_input([prompt]) -> string这里看出，raw_input函数输入的是string类型的。
1、raw_input函数的格式如下所示：
re = raw_input([prompt])--说明：[]符号表示可用可不用
说明：
prompt：指提示字符
re：返回值


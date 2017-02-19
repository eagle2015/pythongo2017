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


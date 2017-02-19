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

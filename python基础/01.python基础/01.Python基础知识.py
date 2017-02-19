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
    Python是一种解释型、面向对象、动态数据类型的高级程序设计语言。自从20世纪90年代初Python语言诞生至今，它逐渐被广泛应用于处理系统管理任务和Web编程。
Python是完全面向对象的语言。函数、模块、数字、字符串都是对象。并且完全支持继承、重载、派生、多继承，有益于增强源代码的复用性。Python支持重载运算符和动态类型。
2、Python的设计理念
    Python的设计哲学是“优雅”、“明确”、“简单”。因此，Perl语言中“总是有多种方法来做同一件事”的理念在Python开发者中通常是难以忍受的。
Python开发者的哲学是“用一种方法，最好是只有一种方法来做一件事”。
3、Python的标准库
    Python拥有一个强大的标准库。Python语言的核心只包含数字、字符串、列表、字典、文件等常见类型和函数，
而由Python标准库提供了系统管理、网络通信、文本处理、数据库接口、图形系统、XML处理等额外的功能。Python标准库命名接口清晰、文档良好，很容易学习和使用。
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
（2）PyCharm[6]：详见百度百科PyCharm，由著名的JetBrains公司开发，带有一整套可以帮助用户在使用Python语言开发时提高其效率的工 具，
比如调试、语法高亮、Project管理、代码跳转、智能提示、自动完成、单元测试、版本控制。此外，该IDE提供了一些高级功能，以用于支持Django框架下的专业Web开发。
（3）PythonWin：ActivePython或pywin32均提供该IDE，仅适用于Windows
（4）PyPE：一个开源的跨平台的PythonIDE。
（5）eclipse + pydev插件：方便调试程序
（6）emacs：自带python支持，自动补全、refactor等功能需要插件支持
（7）Vim: 最新7.3版编译时可以加入python支持，提供python代码自动提示支持
（8）Visual Studio 2010 + Python Tools for Visual Studio
（9）TextMate
（10）Netbeans IDE
    另外，诸如EditPlus、UltraEdit等通用的程序员文本编辑器软件也能对Python代码编辑提供一定的支持，比如代码自动着色、注释快捷键等，
但是否够得上集成开发环境的水平，尚有待评估。
5、Python常见的解释器
（1）Python
    是一门跨平台的脚本语言，Python规定了一个Python语法规则，实现了Python语法的解释程序就成为了Python的解释器。
（2）CPython
   ClassicPython，也就是原始的Python实现，需要区别于其他实现的时候才以CPython称呼；或解作C语言实现的Python。这是最常用的Python版本。
（3）Jython
   原名JPython；Java语言实现的Python，现已正式发布。Jython可以直接调用Java的各种函数库。
（4）PyPy
   使用Python语言写的Python。


python是一门什么语言

编程语言主要从以下几个角度进行分类：

编译型和解释型

静态语言和动态语言

强类型定义语言和弱类型语言


编译型和解释型：

       编译型，其实他和汇编语言是一样的：也是有一个负责翻译的程序来对我们的源代码进行转换，生成相对应的可执行代码。
这个说的更专业一点，就是编辑（Complie），而负责编译的程序自然就称谓编译器（Compiler）。如果我们写的程序代码都包含在一个源文件中，
那么通常编译之后就会生成一个可执行文件，我们就直接运行了，而对于一个比较复杂的项目，为了方便管理，我们通常把代码分散在各个原文件中，作为不同的模块来组织。
这是编译各个文件时就会生成目标文件（Objecfile）而不是之前所说的可执行文件。
   一般一个源文件的编译都会对应一个目标文件。这些目标文件里的内容基本上已经是可执行代码了，但是由于只是整个项目的一部分，所以我们还不能直接运行。
待所有的源文件编译都大功告成，我们就可以最后把这些半成品的目标文件“打包”成一个可执行文件了，这个工作由另一个程序负责完成，
由于过程好像是把包含可执行代码的目标文件连接装配起来，所以这个操作又称为连接（Link），而负责连接的程序就叫。。。。。连接程序 （Linker）。
连接程序除了连接文件之外，可能还有各种资源，图标文件啊、声音等。连接完成后，一般就可以得到我们降妖的可执行文件了。

上面我们大概介绍了编译型语言的特点，现在在看看解释性。从字面上来看“编译”和“解释”都有“翻译”的意思，他们的区别则在于翻译的时机不一样。
打个比方：如果你打算预读一本外文书，而你不知道这么外语，那么你可以找一名翻译，给他足够的时间让他从头到尾把整本书翻译好，
然后把书的母语版交给你阅读。这个过程就编译，或者你也立刻让这名翻译辅助你阅读，让他一句一句的给你翻译，如果你想往回看某个章节他也的重新给你翻译。

两种方式：前者就相当于我们刚才说的编译型：一次把所有的代码转换成机器语言，然后写成可执行文件。

而后者就相当于：在程序运行的前一刻， 还只有源程序而没有可执行程序；而程每执行到资源程序的某一条执行，则会有一个称之为解释程序的外壳程序，
将源代码转换成二进制代码以供执行，总而言之就是不断的解释、执行、解释、执行。。。所以解释型语言是离不开解释程序的。

由于程序总是以源代码的形式出现，因此只要有相应的解释器，一直几乎不成问题。编译型程序虽然源代码也可以执行，但前提必须针对不通的系统分别进行编译，
对于复杂的工程来说，的确是一件不小的时间小号，而且何忧可能一些细节的地方还有修改源代码。

但是解释性程序省却了编译的步骤，修改调试也非常方便，编辑完毕之后即可运行，不必想编译型语言修改了小小的改动要等很长的Compiling...Linking...
不过凡是有利有弊，由于解释性程序试讲编译的过程放在执行过程中，这就决定了解释性程序注定要比编译型慢上一大截，就想几百倍的速度差距也不足为奇
但既然编译型与解释性各有优缺点又相互对立，所以一批新星的语言都有把两者折中起来的趋势，例如Java语言虽然比较接近解释性语言的特性，但在执行之前预
先进行一次预编译，生成的代码是介于机器码和Java源代码之间的中介码，运行的时候而又JVM（Java的虚拟机平台，可视为解释器）解释执行。他即保
留了源代码的高抽象、可抑制的特点，又已完成了对源代码的大部分预编译工作，所以执行起来比“纯解释性”程序要快的多。宗旨，随着设计技术与硬件的不断发
展，编译型与解释性两种方式的界限正在不断的变模糊

静态语言和动态语言：

通常我们所说的动态语言、静态语言是指动态类型语言和静态类型语言。

1、 动态类型语言：动态类型语言是指在运行期间才去做数据类型检查的语言，也就是说，在动态类型的语言编程时，永远也不用给任何变量指定数据类型，该语言会在
第一次赋值给变量是，在内部将数据类型记录下来。Python和Ruby就是典型类型的动态类型语言，其他的各种脚本语言如VBScript也多少属于动
态类型语言。

2、静态类型语言：静态类型语言与动态类型语言刚好相反，他的数据类型是在编译期间检查的，也就是说在写程序的时候要声明所有变量的数据类型，
C / C + +是静态类型的典型代表，其他的静态类型语言还有C  # 、JAVA等

对于动态语言与静态语言的区分，套用一句比较流行的话是：Static
typing
when
possible, dynamic
typing
when
needed

强类型定义语言和弱类型语言

1、强类型定义语言：强制数据类型定义的语言。也就是说，一旦一个变量被指定了某个数据类型，如果不经过强制转换，那么他就永远是这个数据类型了。
举个例子：如果你定义了一个整形变量a，那么程序根本不可能讲a当作字符串类型处理。强类型定义语言是类型安全的语言。

2、弱类型定义语言：数据类型可以被忽略的语言。他与强类型定义语言相反，一个变量可以赋予不同数据类型。



强类型定义语言在速度上可能略逊色与弱类型定义语言，但是他是强类型定义语言带来的严谨性能够有效便面许多错误
，另外，“这么语言是不是动态语言”与“这么语言是否类型安全”之间是完全没有联系的。

例如：Python是动态语言，也是强类型定义语言（类型安全的语言）；VBScript是动态语言是弱类型定义语言（类型不安全的语言）；

JAVA是静态语言，是强类型定义语言（类型安全的语言）




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

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict  =  {'age': 27, 'Work': 'PE', 'Name': 'fly', 'Sex': 'female'}

print dict['one']  # 输出键为'one' 的值
print dict[2]  # 输出键为 2 的值
print tinydict  # 输出完整的字典
print tinydict.keys()  # 输出所有键
print tinydict.values()  # 输出所有值

Python数字
Python 数字数据类型用于存储数值。

数据类型是不允许改变的,这就意味着如果改变数字数据类型得值，将重新分配内存空间。
Python 支持四种不同的数值类型
1、整型(Int)
      通常被称为是整型或整数，是正或负整数，不带小数点。
2、长整型(long integers)
      无限大小的整数，整数最后是一个大写或小写的L。
3、浮点型(floating point real values)
      浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）
4、复数( (complex numbers))
      复数的虚部以字母J 或 j结尾 。如：2+3i

注意：
1、长整型也可以使用小写"L"，但是还是建议您使用大写"L"，避免与数字"1"混淆。Python使用"L"来显示长整型。
2、Python还支持复数，复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型

三、Python数字类型转换
int(x [,base ])         将x转换为一个整数
long(x [,base ])        将x转换为一个长整数
float(x )               将x转换到一个浮点数
complex(real [,imag ])  创建一个复数
str(x )                 将对象 x 转换为字符串
repr(x )                将对象 x 转换为表达式字符串
eval(str )              用来计算在字符串中的有效Python表达式,并返回一个对象
tuple(s )               将序列 s 转换为一个元组
list(s )                将序列 s 转换为一个列表
chr(x )                 将一个整数转换为一个字符
unichr(x )              将一个整数转换为Unicode字符
ord(x )                 将一个字符转换为它的整数值
hex(x )                 将一个整数转换为一个十六进制字符串
oct(x )                 将一个整数转换为一个八进制字符串


Python数学函数
函数	返回值 ( 描述 )
abs(x)	返回数字的绝对值，如abs(-10) 返回 10
ceil(x)	返回数字的上入整数，如math.ceil(4.1) 返回 5
cmp(x, y)	如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1
exp(x)	返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
fabs(x)	返回数字的绝对值，如math.fabs(-10) 返回10.0
floor(x)	返回数字的下舍整数，如math.floor(4.9)返回 4
log(x)	如math.log(math.e)返回1.0,math.log(100,10)返回2.0
log10(x)	返回以10为基数的x的对数，如math.log10(100)返回 2.0
max(x1, x2,...)	返回给定参数的最大值，参数可以为序列。
min(x1, x2,...)	返回给定参数的最小值，参数可以为序列。
modf(x)	返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
pow(x, y)	x**y 运算后的值。
round(x [,n])	返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
sqrt(x)	返回数字x的平方根，数字可以为负数，返回类型为实数，如math.sqrt(4)返回 2+0j

Python随机数函数
        随机数可以用于数学，游戏，安全等领域中，还经常被嵌入到算法中，用以提高算法效率，并提高程序的安全性。
        Python包含以下常用随机数函数：
函数	 描述
choice(seq)	从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
randrange ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
random()	随机生成下一个实数，它在[0,1)范围内。
seed([x])	改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
shuffle(lst)	将序列的所有元素随机排序
uniform(x, y)	随机生成下一个实数，它在[x,y]范围内。


Python三角函数
Python包括以下三角函数：
函数	描述
acos(x)	返回x的反余弦弧度值。
asin(x)	返回x的反正弦弧度值。
atan(x)	返回x的反正切弧度值。
atan2(y, x)	返回给定的 X 及 Y 坐标值的反正切值。
cos(x)	返回x的弧度的余弦值。
hypot(x, y)	返回欧几里德范数 sqrt(x*x + y*y)。
sin(x)	返回的x弧度的正弦值。
tan(x)	返回x弧度的正切值。
degrees(x)	将弧度转换为角度,如math.degrees(math.tan(1.0)) ,返回30.0
radians(x)	将角度转换为弧度
七、Python数学常量
常量	描述
pi	数学常量 pi（圆周率，一般以π来表示）
e	数学常量 e，e即自然常数（自然常数）。

Python字符串
字符串是最 Python 总常用的数据类型。我们可以使用引号来创建字符串。
创建字符串很简单，只要为变量分配一个值即可。

二、Python访问字符串中的值
Python不支持单字符类型，单字符也在Python也是作为一个字符串使用。
Python访问子字符串，可以使用方括号来截取字符串，

'''
#!/usr/bin/python

var1 = 'Hello World!python 2017'
var2 = "Python Programming"

print "var1[0]: ", var1[0]
print "var2[1:6]: ", var2[1:6]
'''


三、Python字符串更新
可以对已存在的字符串进行修改，并赋值给另一个变量，如下实例:

'''

#!/usr/bin/python

var1 = 'Hello World!'
print "Updated String :- ", var1[:6] + 'Python'
'''
'''
实例执行结果:
Updated String :-  Hello Python
'''

Python转义字符
在需要在字符中使用特殊字符时，python用反斜杠(\)转义字符。如下表：
转义字符	描述
\(在行尾时)	续行符
\\	反斜杠符号
\'	单引号
\"	双引号
\a	响铃
\b	退格(Backspace)
\e	转义
\000	空
\n	换行
\v	纵向制表符
\t	横向制表符
\r	回车
\f	换页
\oyy	八进制数yy代表的字符，例如：\o12代表换行
\xyy	十进制数yy代表的字符，例如：\x0a代表换行
\other	其它的字符以普通格式输出


Python字符串运算符:

操作符	描述	实例
+	字符串连接	a + b 输出结果： HelloPython
*	重复输出字符串	a*2 输出结果：HelloHello
[]	通过索引获取字符串中字符	a[1] 输出结果 e
[ : ]	截取字符串中的一部分	a[1:4] 输出结果 ell
in	成员运算符 - 如果字符串中包含给定的字符返回 True	H in a 输出结果 1
not in	成员运算符 - 如果字符串中不包含给定的字符返回 True	M not in a 输出结果 1
r/R	原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。
    原始字符串除在字符串的第一个引号前加上字母"r"（可以大小写）以外，与普通字符串有着几乎完全相同的语法。
    print r'\n' prints \n 和 print R'\n'prints \n
%	格式字符串

Python字符串格式化
       Python 支持格式化字符串的输出 。尽管这样可能会用到非常复杂的表达式，但最基本的用法是将一个值插入到一个有字符串格式符 %s 的字符串中。

'''
#!/usr/bin/python

print "My name is %s and weight is %d kg!" % ('flying', 51)


'''

python字符串格式化符号:

符   号	描述
      %c	 格式化字符及其ASCII码
      %s	 格式化字符串
      %d	 格式化整数
      %u	 格式化无符号整型
      %o	 格式化无符号八进制数
      %x	 格式化无符号十六进制数
      %X	 格式化无符号十六进制数（大写）
      %f	 格式化浮点数字，可指定小数点后的精度
      %e	 用科学计数法格式化浮点数
      %E	 作用同%e，用科学计数法格式化浮点数
      %g	 根据值的大小决定使用%f活%e
      %G	 作用同%g，根据值的大小决定使用%f活%e
      %p	 用十六进制数格式化变量的地址

格式化操作符辅助指令:
符号	功能
*	定义宽度或者小数点精度
-	用做左对齐
+	在正数前面显示加号( + )
<sp>	在正数前面显示空格
#	在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
0	显示的数字前面填充'0'而不是默认的空格
%	'%%'输出一个单一的'%'
(var)	映射变量(字典参数)
m.n.	m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)

八、Python三引号（triple quotes）
python中三引号可以将复杂的字符串进行复制
python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。
三引号的语法是一对连续的单引号或者双引号（通常都是成对的用）。

三引号让程序员从引号和特殊字符串的泥潭里面解脱出来，自始至终保持一小块字符串的格式是所谓的WYSIWYG（所见即所得）格式的。
        一个典型的用例是，当你需要一块HTML或者SQL时，这时用字符串组合，特殊字符串转义将会非常的繁琐。

Unicode 字符串
      Python 中定义一个 Unicode 字符串和定义一个普通字符串一样简单：

>>> u'Hello World !'
u'Hello World !'


引号前小写的"u"表示这里创建的是一个 Unicode 字符串。如果你想加入一个特殊字符，可以使用 Python 的 Unicode-Escape 编码。如下例所示：
>>> u'Hello\u0020World !'
u'Hello World !'

被替换的 \u0020 标识表示在给定位置插入编码值为 0x0020 的 Unicode 字符（空格符）。


python的字符串内建函数
        字符串方法是从python1.6到2.0慢慢加进来的——它们也被加到了Jython中。
        这些方法实现了string模块的大部分方法，如下表所示列出了目前字符串内建支持的方法，所有的方法都包含了对Unicode的支持，有一些甚至是专门用于Unicode的。



方法	描述
string.capitalize()  把字符串的第一个字符大写
string.center(width) 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
string.count(str, beg=0, end=len(string)) 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
string.decode(encoding='UTF-8', errors='strict') 以encoding指定的编码格式解码string,如果出错默认报一个ValueError的异常,除非errors指定的是'ignore'或者'replace'
string.encode(encoding='UTF-8', errors='strict') 以encoding指定的编码格式编码string，如果出错默认报一个ValueError的异常，除非errors指定的是'ignore'或者'replace'
string.endswith(obj, beg=0, end=len(string))检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
string.expandtabs(tabsize=8) 把字符串 string 中的 tab 符号转为空格，默认的空格数 tabsize 是 8.
string.find(str, beg=0, end=len(string))检测 str 是否包含在 string 中，如果 beg和 end指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1
string.index(str, beg=0, end=len(string)) 跟find()方法一样，只不过如果str不在 string中会报一个异常.
string.isalnum() 如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
string.isalpha() 如果 string 至少有一个字符并且所有字符都是字母则返回 True,否则返回 False
string.isdecimal() 如果 string 只包含十进制数字则返回 True 否则返回 False.
string.isdigit() 如果 string 只包含数字则返回 True 否则返回 False.
string.islower() 如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
string.isnumeric() 如果 string 中只包含数字字符，则返回 True，否则返回 False
string.isspace() 如果 string 中只包含空格，则返回 True，否则返回 False.
string.istitle() 如果 string 是标题化的(见 title())则返回 True，否则返回 False
string.isupper() 如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
string.join(seq) Merges (concatenates)以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
string.ljust(width) 返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
string.lower() 转换 string 中所有大写字符为小写.
string.lstrip() 截掉 string 左边的空格
string.maketrans(intab, outtab])
maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
max(str) 返回字符串 str 中最大的字母。
min(str) 返回字符串 str 中最小的字母。
string.partition(str)有点像 find()和 split()的结合体,从 str 出现的第一个位置起,把字符串string分成一个3元素的元组 (string_pre_str,str,string_post_str),
                                                   如果 string 中不包含str 则 string_pre_str == string.

string.replace(str1, str2,  num=string.count(str1)) 把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次.

string.rfind(str, beg=0,end=len(string) )类似于 find()函数，不过是从右边开始查找.
string.rindex( str, beg=0,end=len(string))类似于 index()，不过是从右边开始.
string.rjust(width) 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
string.rpartition(str)类似于 partition()函数,不过是从右边开始查找.
string.rstrip()删除 string 字符串末尾的空格.
string.split(str="", num=string.count(str))以 str 为分隔符切片 string，如果 num有指定值，则仅分隔 num 个子字符串
string.splitlines(num=string.count('\n'))按照行分隔，返回一个包含各行作为元素的列表，如果 num 指定则仅切片 num 个行.
string.startswith(obj, beg=0,end=len(string))检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查.
string.strip([obj])在 string 上执行 lstrip()和 rstrip()
string.swapcase()翻转 string 中的大小写
string.title()返回"标题化"的 string,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
string.translate(str, del="")根据 str 给出的表(包含 256 个字符)转换 string 的字符,要过滤掉的字符放到 del 参数中
string.upper()转换 string 中的小写字母为大写
string.zfill(width)返回长度为 width 的字符串，原字符串 string 右对齐，前面填充0
string.isdecimal()  isdecimal()方法检查字符串是否只包含十进制字符。这种方法只存在于unicode对象。



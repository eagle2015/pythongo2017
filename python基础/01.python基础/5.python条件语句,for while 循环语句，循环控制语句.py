Python条件语句

一、Python 条件语句
        Python条件语句是通过一条或多条语句的执行结果（True或者False）来决定执行的代码块。
注意：  Python程序语言指定任何非0和非空（null）值为true，0 或者 null为false。

二、Python条件语句的基本形式（if .elif..else..）
       Python 编程中 if 语句用于控制程序的执行，基本形式为：

if 判断条件：
    执行语句……
else：
    执行语句……

说明：
       其中"判断条件"成立时（非零），则执行后面的语句，而执行内容可以多行，以缩进来区分表示同一范围。
       else 为可选语句，当需要在条件不成立时执行内容则可以执行相关语句
       具体例子如下：
'''
# !/usr/bin/python
# coding:utf-8

flag = False
name = 'flying'

if name == 'python':  # 判断变量否为'python'
    flag = True  # 条件成立时设置标志为真
    print 'welcome boss'  # 并输出欢迎信息
else:
    print name  # 条件不成立时输出变量名称

'''

if 语句的判断条件可以用 >（大于）、 < (小于)、 == （等于）、 >= （大于等于）、 <= （小于等于）来表示其关系。

三、Python条件语句的基本形式（if ...elif...else）
当判断条件为多个值是，可以使用以下形式：

if 判断条件1:
    执行语句1……
elif 判断条件2:
    执行语句2……
elif 判断条件3:
    执行语句3……
else:
    执行语句4……


'''
num = int(raw_input("please in numble:"))
while True:
    if num == 13:            # 判断num的值
        print 'boss'
        break
    elif num == 12:
        print 'user'
        break
    elif num == 1:
        print 'worker'
        break
    elif num > 50:           # 值小于零时输出
        print 'error,you input num is big'
        break
    else:
        print 'roadman'     # 条件均不成立时输出
        exit()

'''

四、Python多个条件判断
    由于 python 并不支持 switch 语句，所以多个条件判断，只能用 elif 来实现，如果判断需要多个条件需同时判断时，
    可以使用 or （或），表示两个条件有一个成立时判断条件成功；使用 and （与）时，表示只有两个条件同时成立的情况下，判断条件才成功。
num = 9
if num >= 0 and num <= 100:  # 判断值是否在0~10之间
    print 'hello python !2017 '

num = 10
if num < 0 or num > 10:  # 判断值是否在小于0或大于10
    print 'hello'
else:
    print 'undefine '

num = 18
# 判断值是否在0~5或者10~15之间
if (num >= 0 and num <= 5) or (num >= 10 and num <= 25):
    print 'hello go 2017 !'
else:
    print 'undefine'


'''
hello python !2017
undefine
hello go 2017 !

'''

当if有多个条件时可使用括号来区分判断的先后顺序，括号中的判断优先执行，此外 and 和 or 的优先级低于>（大于）、<（小于）等判断符号，
即大于和小于在没有括号的情况下会比与或要优先判断。

五、简单的语句组
      我们可以在同一行的位置上使用if条件判断语句，如下实例：

    var = 100
    if (var == 100): print "Value of expression is 100"
    print "Good bye!python 2017"


Python for  循环语句

    一、循环语句的一般形式:
    循环语句允许我们执行一个语句或语句组多次，
    Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。

    一、Python for循环语法
    Python  for循环的语法格式如下：
    for iterating_var in sequence:
        statements(s)

'''
#!/usr/bin/python

for letter in 'Python':     # First Example
   print 'Current Letter :', letter

fruits = ['banana', 'apple',  'mango','orage']
for fruit in fruits:        # Second Example
   print 'Current fruit :', fruit

print "Good bye!"
'''

三、通过序列索引迭代
另外一种执行循环的遍历方式是通过索引，如下实例：
'''
#!/usr/bin/python

fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print 'Current fruit :', fruits[index]

print "Good bye!"
'''
说明：
       以上实例我们使用了内置函数 len() 和 range(),函数 len() 返回列表的长度，即元素的个数。 range返回一个序列的数。


四、循环使用 else 语句
       在 python 中，for … else 表示这样的意思，for 中的语句和普通的没有区别，else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，while … else 也是一样。
如下实例：


'''
#!/usr/bin/python

for num in range(11,20):  #to iterate between 11 to 20
   for i in range(2,num): #to iterate on the factors of the number
      if num%i == 0:      #to determine the first factor
         j=num/i          #to calculate the second factor
         print '%d equals = %d * %d' % (num,i,j)
         break #to move to the next number, the #first FOR
   else:                  # else part of the loop
      print num, 'is a prime number'

'''


'''

11 is a prime number
12 equals = 2 * 6
13 is a prime number
14 equals = 2 * 7
15 equals = 3 * 5
16 equals = 2 * 8
17 is a prime number
18 equals = 2 * 9
19 is a prime number
'''

Python for 循环嵌套语法:
所谓Python 循环嵌套，是指Python 语言允许在一个循环体里面嵌入另一个循环。
一、Python for 循环嵌套语法（一）

for iterating_var in sequence:
    for iterating_var in sequence:
        statements(s)
    statements(s)


二、Python while 循环嵌套语法（二）
while expression:
    while expression:
        statement(s)
    statement(s)

你可以在循环体内嵌入其他的循环体，如在while循环中可以嵌入for循环， 反之，你可以在for循环中嵌入while循环。

三、实例
以下实例使用了嵌套循环输出1~50之间的素数：
i = 1
while (i < 50):
    j = 2
    while (j <= (i / j)):
        if not (i % j): break
        j = j + 1
    if (j > i / j): print i, " 是素数"
    i = i + 1

print "Good bye! python 2017"

'''
1  是素数
2  是素数
3  是素数
5  是素数
7  是素数
11  是素数
13  是素数
17  是素数
19  是素数
23  是素数
29  是素数
31  是素数
37  是素数
41  是素数
43  是素数
47  是素数
'''


二、Python的for循环和while循环
    Python提供了for循环和while循环（在Python中没有do..while循环）:
    循环类型     描述
    while 循环    在给定的判断条件为 true 时执行循环体，否则退出循环体。
    for 循环       重复执行语句
    嵌套循环       你可以在while循环体中嵌套for循环

三、循环控制语句
循环控制语句可以更改语句执行的顺序。Python支持以下循环控制语句：
控制语句	描述
break 语句	    在语句块执行过程中终止循环，并且跳出整个循环
continue 语句	在语句块执行过程中终止当前循环，跳出该次循环，执行下一次循环。
pass 语句	    pass是空语句，是为了保持程序结构的完整性。

Python break 语句
Python break语句，就像在C语言中，打破了最小封闭for或while循环。
break语句用来终止循环语句，即循环条件没有False条件或者序列还没被完全递归完，也会停止执行循环语句。break语句用在while和for循环中。
如果您使用嵌套循环，break语句将停止执行最深层的循环，并开始执行下一行代码。

'''
for letter in 'Python':  # First Example
    if letter == 'o':
        break
    print 'Current Letter :', letter

var = 100  # Second Example
while var > 0:
    var = var - 10
    if var == 60:
        continue
        # "var=60,continue"
    elif var == 50:
        pass
        print 'This is pass block'
    elif var == 20:
        break
    print 'Current variable value :', var
print "Good bye!python 2017"
'''

Python continue 语句
Python continue 语句跳出本次循环，而break跳出整个循环。continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。
       continue语句用在while和for循环中。

'''
Current Letter : P
Current Letter : y
Current Letter : t
Current Letter : h
Current variable value : 90
Current variable value : 80
Current variable value : 70
Current variable value : 50
Current variable value : 40
Current variable value : 30
Good bye!python 2017
'''


ython pass是空语句，是为了保持程序结构的完整性。

一、Python 语言 pass 语句语法格式
pass




流程控制
if else 语句 实现逻辑控制
    if(判断真假):
        如果是真 执行 （缩进）
    else：
        如果是假 执行
    这里的语句，和if无关 都会执行

逻辑控制 多层if判断
            x = raw_input('please enter you name ')
            if x=='flying':
                print 'you are a nice girl!'
            elif x=='eagle':
                print 'you are nice too!'
            else:
                print 'nice to meet you'
逻辑控制 if可以嵌套多层 (多层缩进)
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



Python While循环语句
一、Python While循环的基本形式
Python 编程中 while 语句用于循环执行程序，即在某条件下，循环执行某段程序，以处理需要重复处理的相同任务。
其基本形式为：
while 判断条件：
    执行语句……
执行语句可以是单个语句或语句块。

二、Python While循环的执行流程图
判断条件可以是任何表达式，任何非零、或非空（null）的值均为true。
当判断条件假false时，循环结束。
'''
#!/usr/bin/python

count = 0
while (count < 10):
   print 'The count is:', count
   count = count + 1
print "Good bye!"
'''

2、continue和break
while 语句时还有另外两个重要的命令 continue，break 来跳过循环。
continue 用于跳过该次循环，
break 则是用于退出循环，此外"判断条件"还可以是个常值，表示循环必定成立。
具体用法如下：
'''
i = 1
while i < 11:
    i += 1
    if i%2 > 0:     # 非双数时跳过输出
        continue
    print i         # 输出双数2、4、6、8、10

'''

'''
i = 1
while 1:            # 循环条件为1必定成立
    print i         # 输出1~10
    i += 1
    if i > 10:     # 当i大于10时跳出循环
        break
'''

3、无限循环
如果条件判断语句永远为 true，循环将会无限的执行下去，如下实例：

'''
#!/usr/bin/python

var = 1
while var == 1 :  # 该条件永远为true，循环将无限执行下去
   num = raw_input("Enter a number  :")
   print "You entered: ", num

print "Good bye! python 2017"
'''

注意：
        以上的无限循环你可以使用 CTRL+C 来中断循环。

4、循环使用 else 语句
      在 python 中，for … else 表示这样的意思，for 中的语句和普通的没有区别，else 中的语句会在循环正常执行完
      （即 for 不是通过 break 跳出而中断的）的情况下执行，while … else 也是一样。
例子：

'''
count = 0
while count < 15:
   print count, " is  less than 15"
   count = count + 1
else:
   print count, " is not less than 15"
'''
5、简单语句组
类似if语句的语法，如果你的while循环体中只有一条语句，你可以将该语句与while写在同一行中， 如下所示：

'''
#!/usr/bin/python

flag = 10
while (flag): print 'Given flag is really true!'
print "Good bye!python 2017"
'''
注意：
       以上的无限循环你可以使用 CTRL+C 来中断循环。
--------------------------------------------------------------------------------------------------------------------------
while循环: 一直循环执行语句,注意缩进
#注意缩进
while 判断条件:
      #如果判断条件是真，循环体的语句就会一直执行
      语句1
      语句2
     修改判断条件中的变量，使得循环是可以结束的
这里的语句，和wilie无关（缩进）



while循环
            i=0
            while i< 100:
                print i
                i = i + 1
while循环
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



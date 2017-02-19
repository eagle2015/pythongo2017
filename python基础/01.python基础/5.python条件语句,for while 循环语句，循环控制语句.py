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

    二、Python的for循环和while循环
    Python提供了for循环和while循环（在Python中没有do..while循环）:
    循环类型
    描述
    while 循环    在给定的判断条件为 true 时执行循环体，否则退出循环体。
    for 循环       重复执行语句
    嵌套循环       你可以在while循环体中嵌套for循环

三、循环控制语句
循环控制语句可以更改语句执行的顺序。Python支持以下循环控制语句：
控制语句	描述
break 语句	在语句块执行过程中终止循环，并且跳出整个循环
continue 语句	在语句块执行过程中终止当前循环，跳出该次循环，执行下一次循环。
pass 语句	pass是空语句，是为了保持程序结构的完整性。


流程控制

if else 语句 实现逻辑控制


    if(判断真假):
        如果是真 执行 （缩进）
    else：
        如果是假 执行
    这里的语句，和if无关 都会执行


逻辑控制

多层if判断


            x = raw_input('please enter you name ')
            if x=='flying':
                print 'you are a nice girl!'
            elif x=='eagle':
                print 'you are nice too!'
            else:
                print 'nice to meet you'


逻辑控制

if可以嵌套多层 (多层缩进)


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


循环--while

一直循环执行语句,注意缩进



            #注意缩进
            while 判断条件:
                #如果判断条件是真，循环体的语句就会一直执行
                语句1
                语句2
                修改判断条件中的变量，使得循环是可以结束的
            这里的语句，和wilie无关（缩进）



循环--while


            i=0
            while i< 100:
                print i
                i = i + 1
[slide]

循环--while


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



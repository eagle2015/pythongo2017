为什么要学编程

传统运维(测试，技术支持)现状

一般运维做两三年，会有瓶颈
大公司运维的现状
云的发展，只运维，不会开发，饭碗被抢
容易被开发绑架
开源软件也需要定制性开发


入门学习编程的方法

慢一点 多理解
多练习，记笔记
把编程当作工具，去解决问题，编程是手段，不是目的
碰到问题google baidu
申请github账号，加入开源社区

----------------------
内容简介

变量 语句
python数据类型
四则运算
获取用户的输入
流程控制
循环


----------------------
注释

代码不仅是可执行的，还要可读
代码一行最前面加一个 # 此行内容不会被执行
方便调试和加上代码解释
'''
    #coding=utf-8
    #获取输入的用户名
    x = raw_input('please input you name ')
    # print it
    print x
'''


字符串--用单引号或者双引号包起来

%s占位符，代表一个字符 语法见代码


'''
        x = 'flying'
        y = 'eagle'
        print 'my name is' + x + ' and I am a '+ y
        print 'my name is %s and I am a %s'  %  (x,y)

'''


字符串格式化


            x = 'flying'
            y = 180
            #报错 数字不能和字符串直接想加
            print 'my name is' + x + ' and I am '+ y + ' cm tall'
            # %s 换成%d 占位符 代表一个数字
            print 'my name is %s and I am %d cm tall'  %  (x,y)


and or

A and B，‘且’，A和B都是真的时候，才为真，否则是假
A or B，‘或’，A和B有一个真的时候，就是真，否则是假


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
[slide]

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
                name = raw_input('please enter you name')

            print 'hello python '+name

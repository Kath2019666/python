# variable1 = 2019
# variable2 = '中国梦'
# def print_variable():
#     print(variable1)
#     print(variable2)
#
# def double(data):
#     data = data*2
#     return data
# print_variable()
# print(double(1000))

class ClassA():
    def function1():
        print('报道！我是类A的第一个方法！')
    def function2():
        print('报道！我是类A的第二个方法！')
    def function3():
        print('报道！我是类A的第三个方法！')

ClassA.function1()
ClassA.function2()
ClassA.function3()

class 类A():
    变量1 = 100
    变量2 = -5.83
    变量3 = 'abc'
# 这里需要用print语句，才能把提取出的数值打印到屏幕上
print(类A.变量1)
print(类A.变量2)
print(类A.变量3)

class 类A():
    变量1 = 100
    变量2 = -5.83
    变量3 = 'abc'
类A.变量1 = 99
类A.变量4 = '新增一个变量'
print(类A.变量1)
print(类A.变量4)

class 智能机器人():
    胸围 = 33
    腰围 = 44
    臀围 = 55
    智商 = 200

    # 以上为类属性
    def 打招呼():
        print('主人你好！')

    def 卖萌():
        print('主人，求抱抱！')

    def 生气():
        print('主人，我要报警了！')

    def 奔跑():
        print('我快乐的奔跑……奔跑……诶呦喂！撞墙了')

    # 以上为类方法
print('把类的属性打印出来：')
print(智能机器人.胸围)
print(智能机器人.腰围)
print(智能机器人.腰围)
print(智能机器人.智商)
智能机器人.奔跑()

# 请直接运行体验代码
class 类A():
    变量1 = 100
    变量2 = 200

    @classmethod
    def 函数1(cls):
        print(cls.变量1)

        print(cls.变量2)
类A.函数1()

class 智能机器人():
    胸围 = 33
    腰围 = 44
    臀围 = 55

    @classmethod
    def 自报三围(cls):
        print('胸围：'+str(cls.胸围))
        print('腰围：' + str(cls.腰围))
        print('臀围：' + str(cls.臀围))
        print('哈哈哈哈哈，下面粗上面细，我长得像个圆锥')
智能机器人.自报三围()

def add_100(num):
    sum = num + 100
    print('计算结果如下：')
    print(sum)

num = 1
add_100(1)

class add_100():
    def add_100(num):
        sum = num +100
        print('计算结果如下：')
        print(sum)
num = 1
add_100.add_100(num)


一首诗 = ['《卜算子》','我住长江头，','君住长江尾。','日日思君不见君，','共饮长江水。']

def 念诗函数(参数):
    for i in 参数:
        print(i)

念诗函数(一首诗)

class read_poem():
 一首诗 = [ '《卜算子》', '我住长江头，', '君住长江尾。', '日日思君不见君，', '共饮长江水。' ]

    def poem_function(num):
        for i in num:
            print(i)
read_poem.poem_function(一首诗)class read_poem():
 一首诗 = [ '《卜算子》', '我住长江头，', '君住长江尾。', '日日思君不见君，', '共饮长江水。' ]

    def poem_function(num):
        for i in num:
            print(i)
read_poem.poem_function(一首诗)

class read_poem():
 一首诗 = [ '《卜算子》', '我住长江头，', '君住长江尾。', '日日思君不见君，', '共饮长江水。' ]

    @classmethod
    def poem_function(cls):
        for i in cls.一首诗:
            print(i)
read_poem.poem_function()
#
# class 加100类():
#     变量 = 100
#     @classmethod
#     def 加100函数(cls, 参数) :
#         总和 = cls.变量 + 参数
#         print ( '加100函数计算结果如下：' )
#         print ( 总和 )
#
# 参数 = int ( input ( '请输入一个整数：' ) )
# 加100类.加100函数 ( 参数 )

# class read_poem():
#  一首诗 = [ '《卜算子》', '我住长江头，', '君住长江尾。', '日日思君不见君，', '共饮长江水。' ]
#
#     @classmethod
#     def poem_function(cls,参数):
#         print(参数)
#         for i in cls.一首诗:
#             print(i)
# 参数 = '给张三念的诗'
# read_poem.poem_function(参数)
#
#
#
# class 类A():
#
#     pass
#
# 类A.变量1 = 100
# print(类A.变量1)


#
# class 类():
#     @classmethod
#     def 打印类属性(cls):
#         print(cls.变量)
# 类.变量 = input('请输入字符串：')
# 类.打印类属性()
 class  Lucky_num():
     @classmethod
     def store(cls):
         print('好的，我把它存起来，然后翻了888倍还给你：'+str(cls.lucky*888))
 Lucky_num.lucky = int(input('你的幸运数是多少？'))
 Lucky_num.store()

class 类():

    @classmethod
    def 增加类属性(cls):
        cls.变量 = input('请随意输入字符串：')
类.增加类属性()


class 念诗类 () :
    一首诗 = [ '《卜算子》', '我住长江头，', '君住长江尾。', '日日思君不见君，', '共饮长江水。' ]

    @classmethod
    def 念诗函数(cls,参数) :
        cls.参数= input('请输入你想给谁念诗：（用户输入张三）')
        print ( '念给' + cls.参数 + '的诗：' )
        for i in cls.一首诗 :
            print ( i )

念诗类.念诗函数 ( '张三' )


class 成绩单():
    @classmethod
    def 录入成绩单(cls):
        cls.学生姓名 = input('请输入学生姓名：')
        cls.语文_成绩 = int(input('请输入语文成绩：'))
        cls.数学_成绩 = int(input('请输入数学成绩：'))
    @classmethod
    def 打印成绩单(cls):
        print ( cls.学生姓名 + '的成绩单如下：' )
        print ('语文成绩：' + str ( cls.语文_成绩 ) )
        print ('数学成绩：' + str ( cls.数学_成绩 ) )
    @classmethod
    def 打印平均分(cls):
        cls.average_score = (cls.语文_成绩 +cls.数学_成绩)/2
        print(cls.学生姓名+'的平均分是：'+str(cls.average_score))

    @classmethod
    

成绩单.录入成绩单()
成绩单.打印成绩单()
成绩单.打印平均分()

变量1 = 2019
变量2 = '中国梦'
def 打印变量():
# 虽然可以中文命名，但括号依旧要用英文
    print(变量1)
    print(变量2)
def 两倍放大(数据):
    数据 =  数据 * 2
    return 数据
打印变量()
print(两倍放大(1000))


class 类A():
    def 函数1():
        print('报道！我是类A的第一个方法！')
    def 函数2():
        print('报道！我是类A的第二个方法！')
    def 函数3():
        print('报道！我是类A的第三个方法！')
类A.函数1()
类A.函数2()
类A.函数3()

class 类A():
    变量1 = 100
    变量2 = -5.83
    变量3 = 'abc'
# 这里需要用print语句，才能把提取出的数值打印到屏幕上
# print(类A.变量1)
# print(类A.变量2)
# print(类A.变量3)
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
    # 以上为类方法
    def 奔跑():
        print('我快乐地奔跑、奔跑……哎呦喂！撞墙了。')
print('把类的属性打印出来：')
print(智能机器人.胸围)
print(智能机器人.腰围)
print(智能机器人.腰围)
print(智能机器人.智商)
智能机器人.打招呼()
智能机器人.卖萌()
智能机器人.奔跑()

print('主人，我的三围是：')
class 智能机器人():
    胸围 = 33
    腰围 = 44
    臀围 = 55
    智商 = 200

    @classmethod
    def 自报三围(cls):
        print('胸围：'+str(cls.胸围))
        print('腰围:'+str(cls.腰围))
        print ( '臀围:' + str(cls.臀围) )

    def 哈哈哈():
        print('哈哈哈哈哈，下面粗上面细，我长得像个圆锥。')

智能机器人.自报三围()
智能机器人.哈哈哈()

def 加100函数(参数):
    总和 = 参数 + 100
    print('计算结果如下：')
    print(总和)

参数 = 1
加100函数(参数)



class 一首诗1():
    一首诗 = [ '《卜算子》', '我住长江头，', '君住长江尾。', '日日思君不见君，', '共饮长江水。' ]

    @classmethod
    def 念诗函数(cls):
        for i in cls.一首诗:
            print(i)
一首诗1.念诗函数()



class 加100类():
    变量 = 100

    @classmethod
    def 加100函数(cls,参数):
        总和 = cls.变量 + 参数
        print('加100函数计算结果如下：')
        print(总和)
参数 = int(input('请输入一个整数：'))
加100类.加100函数(参数)


# class 加100类 () :
#
#
#     变量 = 100
#
#     @classmethod
#     def 加100函数(cls, 参数1, 参数2, 参数3) :
#         总和 = cls.变量 + 参数1 + 参数2 + 参数3
#         print ( '加100函数计算结果如下：' )
#         print ( 总和 )
#
#
# 参数1 = int ( input ( '请输入一个整数：' ) )
# 参数2 = int ( input ( '请输入一个整数：' ) )
# 参数3 = int ( input ( '请输入一个整数：' ) )
# 加100类.加100函数 ( 参数1, 参数2, 参数3 )

class 一首诗1():
    一首诗 = [ '《卜算子》', '我住长江头，', '君住长江尾。', '日日思君不见君，', '共饮长江水。' ]

    @classmethod
    def 念诗函数(cls,参数):
        print ( '念给' + 参数 + '的诗' )
        for i in cls.一首诗:
            print(i)
参数 = input('请输入名字：')
一首诗1.念诗函数(参数)


# class 类A():
#     pass
#
# 类A.变量1 = 100
# print(类A.变量1)


class 类():
    @classmethod
    def 打印类属性(cls):
        print(cls.变量)
类.变量 = input('请输入字符串：')
类.打印类属性()

class lucky():

    @classmethod
    def double(cls):
        new = cls.num * 888
        print('好的，我把它存了起来，然后翻了888倍还给你：'+str(new))

lucky.num = int(input('你的幸运数是多少？请输入一个整数。'))
lucky.double()

class 类():
    @classmethod
    def 增加类属性(cls):
        cls.变量 = input('请随意输入字符串：')
类.增加类属性()

print('打印新增的类属性：')
print(类.变量)


class 念诗类 () :
    一首诗 = [ '《卜算子》', '我住长江头，', '君住长江尾。', '日日思君不见君，', '共饮长江水。' ]

    @classmethod
    def 念诗函数(cls) :
        cls.参数  = input('请输入你想给谁念诗：（用户输入“张三”）')
        print ( '念给' + cls.参数 + '的诗：' )
        for i in cls.一首诗 :
            print ( i )

念诗类.念诗函数 ()


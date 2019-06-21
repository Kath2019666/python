# 创建一个人事系统类
class hrSystem:
    # 创建存储员工名字的变量 name
    name = ''
    # 创建存储员工工资的变量 salary
    salary = 0
    # 创建存储员工绩效的变量 kpi
    kpi = 0

# 定义录入员工信息的类方法
    @classmethod
    def record(cls, name, salary, kpi):
        cls.name = name
        cls.salary = salary
        cls.kpi = kpi

    @classmethod
    def check_name(cls):

        if cls.name in ['bob', 'candy', 'jon', 'kelly']:
            print('录入正确')
            return 1
        else:
            print('录入错误！'+cls.name+'不是本公司员工')
            return 0

#定义打印员工信息的类方法
    @classmethod
    def print_record(cls):
        if cls.check_name():  # 以 cls.check_name() 的返回值（0或1）作为判断条件。
            print(cls.name + '的工作信息如下：')
            print('本月工资：' + str(cls.salary))
            print('本年绩效：' + str(cls.kpi))
        else:
            print('录入错误！'+cls.name +'不是本公司员工')

    @classmethod
    def kpi_reward(cls):
        if cls.kpi > 95:
            print('恭喜'+cls.name+'评为最佳员工')
        elif 80<= cls.kpi <= 95:
            print('恭喜'+cls.name+'评为优秀员工')
        else:
            print(cls.name+'一般员工，没有奖杯')

hrSystem.record('bob',2000,98)
hrSystem.print_record()

#homework2
class calendar():
    day = {'给父母买礼物':'9：00','学习':'10：00','和朋友聚会':'18：30'}

    @classmethod
    def new(cls):
        del cls.day['给父母买礼物']
        cls.day['写日记'] = '20:00'
        print(cls.day)
calendar.new()






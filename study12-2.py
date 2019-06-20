class 成绩单():
    @classmethod
    def 录入成绩单(cls):
        cls.学生姓名 = input('请输入学生姓名：')
        cls.语文_成绩 = int(input('请输入语文成绩：'))
        cls.数学_成绩 = int(input('请输入数学成绩：'))

    @classmethod
    def 打印成绩单(cls):
        print(cls.学生姓名 + '的成绩单如下：')
        print('语文成绩：'+ str(cls.语文_成绩))
        print('数学成绩：'+ str(cls.数学_成绩))

    @classmethod
    def 打印平均分(cls):
        cls.average = (cls.语文_成绩+cls.数学_成绩)/2
        print(cls.学生姓名+'的平均分是：'+str(cls.average))

    @classmethod
    def 评级(cls):
        if cls.average >= 90:
            print(cls.学生姓名+'的评级是：优')
        elif 80 < cls.average < 90:
            print(cls.学生姓名+'的评级是：良')
        elif 60 < cls.average <80:
            print(cls.学生姓名+'评级是：中')
        else:
            print(cls.学生姓名+'评级是：差')

成绩单.录入成绩单()
成绩单.打印成绩单()
成绩单.打印平均分()
成绩单.评级()




class 成绩单():
    @classmethod
    def 录入成绩单(cls):
        cls.学生姓名 = input('请输入学生姓名：')
        cls.成绩 = int(input('请输入考试成绩：'))

    @classmethod
    def 计算是否及格(cls):
        if cls.成绩 >= 60:
            return '及格'
        else:
            return '不及格'

    @classmethod
    def 考试结果(cls):
        if cls.计算是否及格() == '及格':
            print(cls.学生姓名+'同学通过考试')
        else :
            print(cls.学生姓名 +'清补考')

        # if cls.成绩 >= 60:
        #     print(cls.学生姓名+'考试通过啦')
        # elif cls.成绩 < 60:
        #     print(cls.学生姓名 +'同学需要补考')


成绩单.录入成绩单()
成绩单.考试结果()




# for x in range(10):
#     print(x)
#
#
# n=0
# while n<3:
#     username = input("请输入用户名：")
#     password = input("请输入密码：")
#     if username == 'abc' and password == '123':
#         print("登录成功")
#         break
#     else:
#         n=n+1
#         print("输入有误")
# else:
#     print("你输错了三次，登录失败")

# a = []
# # a.append('A')
# # a.append('B')
# # a.append('C')
# # print(a)

# movie = {
#     '妖猫传':['黄轩','染谷将太'],
#     '无问西东':['章子怡','王力宏','祖峰'],
#     '超时空同居':['雷佳音','佟丽娅']
# }
#
# name = input('请输入演员的名字')
# for i in movie:
#     if name = movie[i]:
#         print(name+'出演了'+i)

# movie = {
#     '妖猫传':['黄轩','染谷将太'],
#     '无问西东':['章子怡','王力宏','祖峰'],
#     '超时空同居':['雷佳音','佟丽娅']
# }
# name=input('你查询的演员是？')
# for i in movie:
#     actors=movie[i]
#     if name in actors:
#         print(name+'出演了'+i)
# import random
#
# guess = ''
#
# while guess  not in ['正面','反面']:
#     print('------猜硬币游戏------')
#     print('猜一猜硬币是正面还是反面？')
#     guess = input('请输入“正面”或“反面”：')
#     if guess == '正面':
#         guess1 = 0
#         guess = guess1
#     if guess == '反面':
#         guess1 = 1
#         guess = guess1
#
# # 随机抛硬币，0代表正面，1代表反面
#     toss = random.randint(0,1)
#
#     print(toss)
#     print(guess)

    # if toss == guess:
    #     print('猜对了！你真棒')
    # else:
    #     print('没猜对，你还有一次机会。')
    #     guess = input('再输一次“正面”或“反面”：')
    #     if toss == guess:
    #         print('你终于猜对了！')
    #     else:
    #         print('大失败！')

# import random
# for i in range(20):
#     toss = random.randint(0,1)
#     print(toss)
#
# age = input('你今年几岁了？')
# print(age)
# print(type(age))
#
# try:
#     age = int(input('请输入一个整数：'))
# except ValueError:
#     print('要输入整数噢')
#
# while 1:
#     try:
#         age = int ( input ( '你今年几岁了？' ) )
#         break
#     except ValueError:
#         print('要输入整数噢')
#     if age  < 18:
#         print('不可以喝酒哦')
# try:
#     num = [1,2,0,3]
#     for x in num:
#         print (6/x)
# except ZeroDivisionError :
#     print('0不可以做除数')

# print('\n欢迎使用除法计算器！\n')
# try:
#     num = int(input('请输入除数'))
#     num1 = int(input('请输入被除数'))
#     a = float(num1)/float(num)
#     print(a)
# except ZeroDivisionError:
#     print('被除数不能为0哦')
# except ValueError:
#     print('不能输入字母哦')

print('\n欢迎使用除法计算器！\n')
try:
    num = int(input('请输入除数'))
    num1 = int(input('请输入被除数'))
    a = float(num1)/float(num)
    print(a)
except Exception:
    print('输入有误请重新输入')
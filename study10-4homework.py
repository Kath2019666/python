#思路：利用字典，把石头剪刀布，匹配：0，1，2

import random
punches = ['石头','剪刀','布']
computer123 = {'石头':0,'剪刀':1,'布':2}
computer456 = random.sample(computer123.keys(),1)
print(computer123[computer456])


"""
computers = {}
for i in range(3): #建立一个字典存放计算机的过程
    punches = ['石头', '剪刀', '布']
    computer_choice = random.choice(punches)
    computers[computer_choice] = i
"""
"""
user_choice = input('请输入你的选择')
user1 = {}
if user_choice == '石头':
    user1[user_choice] = 0
elif user_choice == '剪刀':
    user1[ user_choice ] = 1
elif user_choice == '布':
    user1[ user_choice ] = 2
while user_choice not in punches:
    print('输入有误，请重新输入')

print('------战斗过程-------')
print('电脑的出拳结果为：%s'%computer456)
print('你的出拳结果为：%s'%user_choice)

print('---------结果--------')
if user1[user_choice] = computer123
    """

import random
# 出拳
punches = ['石头','剪刀','布']
computer_choice = random.choice(punches)
user_choice = ''
user_choice = input('请出拳：（石头、剪刀、布）')  # 请用户输入选择
while user_choice not in punches:  # 当用户输入错误，提示错误，重新输入
    print('输入有误，请重新出拳')
    user_choice = input()
# 亮拳
print('————战斗过程————')
print('电脑出了：%s' % computer_choice)
print('你出了：%s' % user_choice)
# 胜负
print('—————结果—————')
if user_choice == computer_choice:  # 使用if进行条件判断
    print('平局！')
elif user_choice == punches[punches.index(computer_choice)-1]:
    print('你赢了！')
else:
    print('你输了')





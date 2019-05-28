def show_role():
    player_life = 100
    player_attack = 35
    enemy_life = 105
    enemy_attack = 33
    print('【玩家】\n血量：%s\n攻击：%s'%(player_life,player_attack))
    print('【敌人】\n血量：%s\n攻击：%s'%(enemy_life,enemy_attack))
show_role()

def fav_num(num1,num2):
    print('我喜欢的数字是%d，还有%d。' % (num1,num2))
def add_num(num1,num2):
    print('这两个数字相加的和为%d。'%(num1+num2))

def main(num1,num2):
    fav_num(num1,num2)
    add_num(num1,num2)

main(3,4)

import random
num = [1,2,3,4,5,6,7,8,9,10]
choice = random.sample(num,3)
print(choice)


import time
def show_role(player_life,player_attack,enemy_life,enemy_attack):
    print('【玩家】\n血量：%s\n攻击：%s'%(player_life,player_attack))
    print('---------------')
    print('【敌人】\n血量：%s\n攻击：%s'%(enemy_life,enemy_attack))
    print('---------------')
time.sleep(2)

def pk_role(player_life,player_attack,enemy_life,enemy_attack):
    while player_life >0 and enemy_life >0:
        player_life = player_life - enemy_attack
        enemy_life = enemy_life - player_attack
        print('你发起了攻击，【敌人】剩余血量%s'%(enemy_life))
        print('敌人向你发起了攻击，【玩家】的血量剩余%s'%(player_attack))
        print('--------------------')
        time.sleep(1)
def show_result(player_life,enemy_life):
    if player_life > 0 and enemy_life >0:
        print('敌人死翘翘了，这局你赢了')
    elif player_life <= 0 and enemy_life >0:
        print('悲催，这局敌人把你干掉了！')
    else:
        print('哎呀，这局你和敌人同归于尽了！')
    print('-----------')
def main(player_life,player_attack,enemy_life,enemy_attack):
    show_role(player_life,player_attack,enemy_life,enemy_attack)
    pk_role(player_life,player_attack,enemy_life,enemy_attack)
    show_result(player_life,enemy_life)
main(100,35,105,33)

import random
player_list = ['【狂血战士】','【森林箭手】','【光明骑士】','【独行剑客】','【格斗大师】','【枪弹专家】']
enemy_list = ['【暗黑战士】','【黑暗弩手】','【骷髅骑士】','【嗜血刀客】','【首席刺客】','【陷阱之王】']
player = random.sample(player_list,3)
enemy = random.sample(enemy_list,3)
print(player)



import random
# 将需要用到的固定变量一起放到代码开头，便于使用和管理。
player_list = [ '【狂血战士】', '【森林箭手】', '【光明骑士】', '【独行剑客】', '【格斗大师】', '【枪弹专家】' ]
players = random.sample ( player_list, 3 )  # 从列表里随机选取三个元素
player_life = {}  # 建立空字典，存放我方角色的血量。
player_attack = {}  # 建立空字典，存放我方角色的攻击。
# 生成角色的属性
for i in range(3):
    life = random.randint ( 100, 180 )  # 从100-180随机生成整数，赋值给变量life
    attack = random.randint ( 30, 50 )  # 从30-50随机生成整数，赋值给变量attack
    player_life[ players[i] ] = life  # 给空字典player_life添加键值对，角色列表players的第0个元素为键，变量life为值
    player_attack[ players[i] ] = attack  # 给空字典player_attack添加键值对，角色列表players的第0个元素为键，变量attack为值
    # ③展示我方的角色信息
print('----------------- 角色信息 -----------------')
print('你的人物：')
for i in range(3):
print('%s  血量：%d  攻击：%d'
%(players[i],player_life[players[i]],player_attack[players[0]]))
print('--------------------------------------------')



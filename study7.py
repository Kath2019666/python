import time
print('【玩家】血量：100 攻击：50')
print('【敌人】血量：100 攻击：30')
print('你发起了攻击，【敌人】剩余血量50')
print('敌人向你发起了攻击，【玩家】剩余血量70')
print('你发起了攻击，【敌人】剩余血量0')
print('敌人向你发起了攻击，【玩家】剩余血量40')
print('敌人死翘翘了，你赢了！')

print('【玩家】\n血量：100\n攻击：50')
print('------------------------')
print('【敌人】\n血量：100\n攻击：30')
print('------------------------')
print('你发起了攻击，【敌人】剩余血量50')
print('敌人向你发起了攻击，【玩家】剩余血量70')
print('------------------------')
print('你发起了攻击，【敌人】剩余血量0')
print('敌人向你发起了攻击，【玩家】剩余血量40')
print('-----------------------')
print('敌人死翘翘了，你赢了！')


import time

print('【玩家】\n血量：100\n攻击：50')
print('------------------------')
print('【敌人】\n血量：100\n攻击：30')
print('------------------------')
print('你发起了攻击，【敌人】剩余血量50')
print('敌人向你发起了攻击，【玩家】剩余血量70')
print('------------------------')
print('你发起了攻击，【敌人】剩余血量0')
print('敌人向你发起了攻击，【玩家】剩余血量40')
print('-----------------------')
print('敌人死翘翘了，你赢了！')


1
import time  #通常import语句会写到代码的开头

print('【玩家】\n血量：100\n攻击：50')
print('------------------------')
time.sleep(9)
#暂停1.5秒，再继续运行后面的代码
print('【敌人】\n血量：100\n攻击：30')
print('------------------------')

import random
#调用random模块，与
a = random.randint(1,100)
# 随机生成1-100范围内（含11和100）的一个整数，并赋值给变量a
print(a)

import random
player1 = random.randint(100,150)
debate = random.randint(30,50)
print('【玩家1】\n攻击力'+str(player1)+'\n血量'+str(debate))

import time, random
player_life = random.randint(100,150)
player_attack = random.randint(30,50)
enemy_life = random.randint(100,150)
enemy_attack = random.randint(30,50)
print('【玩家】\n'+'血量：'+str(player_life)+'\n攻击：'+str(player_attack))
print('------------------------')
time.sleep(1)
print('【敌人】\n'+'血量：'+str(enemy_life)+'\n攻击：'+str(enemy_attack))
print('------------------------')
time.sleep(1)


"""
while (player_life >0) and (enemy_life>0):
    player_life = player_life - enemy_attack
    enemy_life = enemy_life - player_attack
    print('你发起了攻击，【敌人】剩余血量'+str(enemy_life))
    print('敌人向你发起了攻击，【玩家】剩余血量'+str(enemy_life))
    print('------------------------')
    if (player_life >0) and (enemy_life <= 0):
        print('玩家获胜！')
    if (player_life <= 0) and (enemy_life > 0):
        print('敌人获胜！')
    if (player_life <= 0) and (enemy_life <= 0):
        print('平局')

    time.sleep(1.5)
"""

for i in range(3):
    print('现在是第' + str(i + 1) + '局')
    player_life = player_life - enemy_attack
    enemy_life = enemy_life - player_attack
    print('你发起了攻击，【敌人】剩余血量' + str(enemy_life))
    print('敌人向你发起了攻击，【玩家】剩余血量' + str(enemy_life))
    print('------------------------')
    if (player_life > 0) and (enemy_life <= 0):
        print('玩家获胜！')
    elif  (player_life <= 0) and (enemy_life > 0):
        print('敌人获胜！')
    elif (player_life <= 0) and (enemy_life <= 0):
        print('平局')
    time.sleep(1.5)

import time, random

for i in range(1, 4):
    time.sleep(1.5)  # 让局与局之间有较明显的有时间间隔
    print(' \n——————现在是第' + str(i) + '局，ready go!——————')  # 作为局的标记
    player_life = random.randint(100, 150)
    player_attack = random.randint(30, 50)
    enemy_life = random.randint(100, 150)

    enemy_attack = random.randint(30, 50)
# 展示双方角色的属性
    print('【玩家】\n' + '血量：' + str(player_life) + '\n攻击：' + str(player_attack))

    print('------------------------')

    time.sleep(1)

    print('【敌人】\n' + '血量：' + str(enemy_life) + '\n攻击：' + str(enemy_attack))

    print('------------------------')

    time.sleep(1)
    player_victory = 0
    enemy_victory = 0

    if player_life > 0 and enemy_life <= 0:
        player_victory += 1
        print('敌人死翘翘了，你赢了！')
    elif player_life <= 0 and enemy_life > 0:
        enemy_victory += 1
        print('悲催，敌人把你干掉了！')
    else:
        print('哎呀，你和敌人同归于尽了！')

    if player_victory > enemy_victory:
        print('玩家获胜')
    elif player_victory < enemy_victory:
        print('敌人获胜')
    else:
        print('平局')

lucky = 8
print('我的幸运数字是%s' % lucky)
print('我的幸运数字是%d' % 8)
print('我的幸运数字是%s' % '小龙女的生日816')
print('我的幸运数字是%d和%d' % (8,16))

print('我的幸运数字是%d，而且我不知道%d' % (8,16))  #8以整数展示
print('我的幸运数字是%s' % 8)  #8以字符串展示
print(8) #整数8与字符串'8'打印出来的结果是一样的
print('8')

print('我的幸运数字是%s' % '小龙女的生日816')
print('我的幸运数字是%d' % '小龙女的生日816')

#homework
#exercise1

import time
import random

player_victory = 0

enemy_victory = 0

for i in range(1,4):
    time.sleep(1.5)
    print('  \n——————现在是第 %s 局——————' % i)
    player_life = random.randint(100,150)
    player_attack = random.randint(30,50)
    enemy_life = random.randint(100,150)
    enemy_attack = random.randint(30,50)
​
    print('【玩家】\n血量：%s\n攻击：%s' % (player_life,player_attack))
    print('------------------------')
    time.sleep(1)
    print('【敌人】\n血量：%s\n攻击：%s' % (enemy_life,enemy_attack))



import time,random
player_victory =0
enemy_victory= 0

while True:

    for i in range(1,4):
        time.sleep(1.5)
        print('  \n——————现在是第 %s 局——————' % i)
        player_life = random.randint(100, 150)
        player_attack = random.randint(30, 50)
        enemy_life = random.randint(100, 150)
        enemy_attack = random.randint(30, 50)
        print('【玩家】\n血量：%s\n攻击：%s' % (player_life, player_attack))
        print('------------------------')
        time.sleep(1)
        print('【敌人】\n血量：%s\n攻击：%s' % (enemy_life, enemy_attack))
    abc = input('是否要继续游戏?')
    if abc == 'yes':
        print('再来一局')
        continue
    elif abc == 'no':
        break




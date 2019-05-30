"""import random

player_list = ['【狂血战士】','【森林箭手】','【光明骑士】','【独行剑客】','【格斗大师】','【枪弹专家】']
players = random.sample(player_list,3)
player_info = {}

def born_role():
    life = random.randint(100,180)
    attack = random.randint(30,50)
    return life,attack

def show_role():
    for i in range(3):
        player_info[players[i]] = born_role()
    print('-------角色信息-------')
    print('你的人物：')
    for i in range(3):
        print('%s 血量：%d 攻击：%d'%(players[i],player_info[players[i]][0],player_info[players[i]][1]))
    print('----------------')
show_role()
"""

"""
import random
player_list = ['【狂血战士】','【森林箭手】','【光明骑士】','【独行剑客】','【格斗大师】','【枪弹专家】']
enemy_list = ['【暗黑战士】','【黑暗弩手】','【暗夜骑士】','【嗜血刀客】','【首席刺客】','【陷阱之王】']
players1 = random.randint(player_list,3)
enemys1 = random.randint(enemy_list,3)
player_info1 = {}
enemy_info1 = {}

def born_role1():
    a = random.randint(100,180)
    b = random.randint(30,50)
    return a,b

def show_role():
    for i in range(3):
        player_info1[players1[i]] = born_role1()
        enemy_info1[enemys1[i]] = born_role1()
        print('-------角色信息-------' )
        print('你的人物：' )
        for i in range ( 3 ) :
            print ('%s 血量：%d 攻击：%d' % (players1[i], player_info1[players1[i]][0], player_info1[players1[i]][1]))
        print('----------------' )
        print('电脑人物：')
        for i in range(3):
            print('%s 血量：%d 攻击:%d'%(enemys1[i],enemy_info1[enemys1[i]][0],enemy_info1[enemys1[i]][1]))
show_role()
"""
"""
import time, random

player_list = [ '【狂血战士】', '【森林箭手】', '【光明骑士】', '【独行剑客】', '【格斗大师】', '【枪弹专家】' ]
enemy_list = [ '【暗黑战士】', '【黑暗弩手】', '【暗夜骑士】', '【嗜血刀客】', '【首席刺客】', '【陷阱之王】' ]
players = random.sample ( player_list, 3 )
enemies = random.sample ( enemy_list, 3 )
player_info = {}
enemy_info = {}


# 随机生成两种属性
def born_role() :
    life = random.randint ( 100, 180 )
    attack = random.randint ( 30, 50 )
    return life, attack  # return 多个元素时，返回一个元组（昨天课堂有讲）


# 给角色生成随机属性，并展示角色信息。
def show_role() :
    for i in range ( 3 ) :
        player_info[ players[ i ] ] = born_role ()
        enemy_info[ enemies[ i ] ] = born_role ()

    # 展示我方的3个角色
    print ( '----------------- 角色信息 -----------------' )
    print ( '你的人物：' )
    for i in range ( 3 ) :
        print ( '%s  血量：%d  攻击：%d'
                % (players[ i ], player_info[ players[ i ] ][ 0 ], player_info[ players[ i ] ][ 1 ]) )
    print ( '--------------------------------------------' )
    print ( '电脑敌人：' )

    # 展示敌方的3个角色
    for i in range ( 3 ) :
        print ( '%s  血量：%d  攻击：%d'
                % (enemies[ i ], enemy_info[ enemies[ i ] ][ 0 ], enemy_info[ enemies[ i ] ][ 1 ]) )
    print ( '--------------------------------------------' )


show_role ()


import random
player_list = ['【狂血战士】','【森林箭手】','【光明骑士】','【独行剑客】','【格斗大师】','【枪弹专家】']
players = random.sample(player_list,3)
print(players)
for i in range(3):
  order = input('你的'+players[i]+'要第几个上场？（请输入数字1,2,3)')
"""

list1 = ['A','B','C']
dict1 = {}
for i in range(3):
    order = int(input('你要把'+list1[i]+'放在第几位？请输入数字'))
    dict1[order] = list1[i]
print(dict1)
list1 = []
for i in range(1,4):
    list1.append(dict1[i])
print(list1)

# 代码1
list1 = ['A','B','C']
#这里的list1 是全局变量，可以被其他函数使用
def order1():
    list1 = ['C', 'B', 'A']
   # orde1()里的list1是局部变量，其他函数无法使用
def use1():
    print(list1)
# 这里打印的list1是最开头的全局变量
order1()
use1()
# 打印出['A','B','C']

list2 = ['A','B','C']
def order2():
    global list2
    # 将list2定义为全局变量，这样后面的函数调用时，会使用这个变量list2。
    list2 = ['C', 'B', 'A']
def use2():
    print(list2)
    # 这里打印的list2是order2()里的list2
order2()
use2()
# 打印出['C', 'B', 'A']


import random

# 将需要的数据和固定变量放在开头
player_list = [ '【狂血战士】', '【森林箭手】', '【光明骑士】', '【独行剑客】', '【格斗大师】', '【枪弹专家】' ]
enemy_list = [ '【暗黑战士】', '【黑暗弩手】', '【暗夜骑士】', '【嗜血刀客】', '【首席刺客】', '【陷阱之王】' ]
players = random.sample ( player_list, 3 )
enemies = random.sample ( enemy_list, 3 )
player_info = {}
enemy_info = {}


# 随机生成角色的属性
def born_role() :
    life = random.randint ( 100, 180 )
    attack = random.randint ( 30, 50 )
    return life, attack


# 生成和展示角色信息
def show_role() :
    for i in range ( 3 ) :
        player_info[ players[ i ] ] = born_role ()
        enemy_info[ enemies[ i ] ] = born_role ()

    # 展示我方的3个角色
    print ( '----------------- 角色信息 -----------------' )
    print ( '你的人物：' )
    for i in range ( 3 ) :
        print ( '%s  血量：%d  攻击：%d'
                % (players[ i ], player_info[ players[ i ] ][ 0 ], player_info[ players[ i ] ][ 1 ]) )
    print ( '--------------------------------------------' )
    print ( '电脑敌人：' )

    # 展示敌方的3个角色
    for i in range ( 3 ) :
        print ( '%s  血量：%d  攻击：%d'
                % (enemies[ i ], enemy_info[ enemies[ i ] ][ 0 ], enemy_info[ enemies[ i ] ][ 1 ]) )
    print ( '--------------------------------------------' )
    input ( '请按回车键继续。\n' )  # 为了让玩家更有控制感，可以插入类似的代码来切分游戏进程。


# 角色排序，选择出场顺序。
def order_role() :
    global players
    order_dict = {}
    for i in range ( 3 ) :
        order = int ( input ( '你想将 %s 放在第几个上场？(输入数字1~3)' % (players[ i ]) ) )
        order_dict[ order ] = players[ i ]

    players = [ ]
    for i in range ( 1, 4 ) :
        players.append ( order_dict[ i ] )

    print ( '\n我方角色的出场顺序是：%s、%s、%s' % (players[ 0 ], players[ 1 ], players[ 2 ]) )
    print ( '敌方角色的出场顺序是：%s、%s、%s' % (enemies[ 0 ], enemies[ 1 ], enemies[ 2 ]) )


def main() :
    show_role ()
    order_role ()


main ()
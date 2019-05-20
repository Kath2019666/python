# homework7-2
import time, random

player_victory = 0
enemy_victory = 0

while True :

    for i in range ( 1, 4 ) :
        time.sleep ( 1.5 )
        print ( '  \n——————现在是第 {} 局——————'.format ( 1 ) )
        player_life = random.randint ( 100, 150 )
        player_attack = random.randint ( 30, 50 )
        enemy_life = random.randint ( 100, 150 )
        enemy_attack = random.randint ( 30, 50 )
        print ( '【玩家】\n血量：{}\n攻击：{}'.format ( player_life, player_attack ) )
        print ( '------------------------' )
        time.sleep ( 1 )
        print ( '【敌人】\n血量：{}\n攻击：{}'.format ( enemy_life, enemy_attack ) )
    abc = input ( '是否要继续游戏?' )
    if abc == 'yes' :
        print ( '再来一局' )
        continue
    elif abc == 'no' :
        break

for i in range ( 1, 3 ) :
    a = i * 2
    print ( '{}X2={}'.format ( i, a ) )

for i in range ( 1, 4 ) :
    b = i * 3
    print ( '%sX3=%s' % (i, b) )

print ( 'hello', end='' )
print ( 'world' )

print ( 'hello', end='  ' )
print ( 'world' )

print ( 'hello', end='!' )
print ( 'world' )

for i in range ( 1, 3 ) :
    print ( '%d X %d = %d' % (i, 2, i * 2), end='    ' )

for i in range ( 1, 4 ) :
    print ( '%d X %d = %d' % (i, 3, i * 3), end='    ' )

for i in range ( 1, 3 ) :
    print ( '%d X %d = %d' % (i, 2, i * 2), end='  ' )
    # end = '' 用于print中的内容需要在同一行的情况
print ( '' )  # 用来换行
# >>1 X 2 = 2  2 X 2 = 4

for i in range ( 1, 4 ) :
    print ( '%d X %d = %d' % (i, 3, i * 3), end='  ' )
print ( '' )  # 用来换行›
# >>1 X 3 = 3  2 X 3 = 6  3 X 3 = 9›


for i in range ( 1, 10 ) :
    for b in range ( 1, 10 ) :
        c = i * b
        print ( '{}X{}={}'.format ( i, b, c ), end='  ' )
        if i == b :
            print ( '  ' )
            break

for i in range ( 1, 10 ) :
    for j in range ( 1, i + 1 ) :
        print ( '%d X %d = %d' % (j, i, j * i), end='  ' )
    print ( '' )

for i in range ( 1, 10 ) :
    for j in range ( 1, i + 1 ) :
        print ( '%d X %d = %d' % (j, i, i * j), end='  ' )
    print ( '  ' )

# homework
A = [ 91, 95, 97, 99 ]
B = [ 92, 93, 96, 98 ]
list1 = [ 91, 95, 97, 99 ]
list1.extend ( B )  # 合并列表把B里面的内容合并到A里面去
list1.sort ()  # 对列表进行永久排序
print ( list1 )
aver = sum ( A ) / len ( A )
print ( aver )
for i in A :
    if i < aver :
        print ( '低于平均分的成绩为%d' % (i), end='   ' )

aver2 = sum ( B ) / len ( B )
print ( aver2 )

import numpy

score1 = list1
score2 = [ ]

average = numpy.mean ( score1 )
print ( '平均成绩是：{}'.format ( average ) )

for score in score1 :
    if score < average :
        score2.append ( score )
        continue
print ( '低于平均分的成绩有：{}'.format ( score2 ) )

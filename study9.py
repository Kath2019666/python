def pika1():
    print('我喜欢皮卡丘')
pika1()

def pika2(name):
    print('我最喜欢的神奇宝贝是'+name)
pika2('皮卡丘')
pika2('喷火龙')

def pika3(name,person):
    print('我最喜欢的神奇宝贝是'+name)
    print('我最喜欢的驯兽师是'+person)
pika3('可达鸭','小霞')

def tree(Height):
    print('Merry Christmas!')
    for i in range(Height):
        print((Height-i)*2*' '+'o'+ i*'~x~o')
        print(((Height-i)*2-1)*' '+(i*2+1)*'/'+'|'+(i*2+1)*'\\')
tree(4)
tree(8)

def dinner(appetizer,course):
    print('客人点的开胃菜是'+appetizer)
    print('客人点的主食是'+course)
dinner('鹅肝','西冷牛排')

def menu(appetizer,course):
    print('开胃菜'+appetizer)
    print('主食'+course+'\n')
menu('牛肉花生','华美')
menu('华美','加了蜂蜜')

menu(course='牛肉拉面',appetizer='酱爆刷生')

def dinner(appetizer,course,dessert='绿豆沙'):
    print('客人点的开胃菜是'+appetizer)
    print('客人点的主食是'+course)
    print('一份甜品'+dessert)

dinner('鹅肝酱','西冷牛排','银耳羹')

def menu(*barbeque):
    print(barbeque)
menu('烤鸡翅','烤玉米','烤香肠')

def dinner(appetizer,course,*barbeque,dessert='绿豆沙'):
    print('客人点的开胃菜是'+appetizer)
    print('客人点的主食是'+course)
    print('一份甜品'+dessert)
    for i in barbeque:
        print('一份烤串：'+i)

dinner('鹅肝酱','西冷牛排','烤鸡翅','烤玉米','烤土豆')

a = [1,2,3]
print(len(a))

def face(name):
    return name+'的脸蛋'
def body(name):
    return name+'身材'
face('李若彤吧')
body('杨幂')
print('我的梦中情人：'+face('李若彤吧')+"+"+body('杨幂'))


def dog1(name):
    return name + '的蜜桃臀'
def  dog2(name):
    return name + '的傻'
def main(dog0,dog9):
    return '我最喜欢'+dog1(dog0)+'和'+dog2(dog9)
print(main('柯基','哈士奇'))

def lover(name1,name2):
    face = name1 +'的脸蛋'
    body = name2 + '的身材'
    return face,body
a = lover('李若彤','林志玲')
print(a)
print('我的梦中情人：'+a[0]+'+'+a[1])

def fun():
    a ='i am coding'
print(fun())

def fun():
    a = 'i am coding'
    return a
print(fun())

def fun():
    return 'i am coding'
    return 'i am not a coding'
print(fun())

def number(number1,number2):
    if number1 > number2:
        return number1
    elif number1 < number2:
        return number2
    else:
        return print('一样大')
print(number(99**2,8888))

x = 99
def num():
    x = 88
    print(x)
num()
print(x)

def egg():
    quantity = 108
egg()
print(egg())

quantity = 108
def egg():
    print(quantity)
egg()


#homework9-1
def hellokitty():
    import random,time
    luckylist = ['派大星','海绵宝宝','章鱼哥']
    a = random.choice(luckylist)
    print('开奖倒计时',3)
    time.sleep(1.5)
    print('开奖倒计时',2)
    time.sleep(1.5)
    print('开奖倒计时',1)
    time.sleep(1.5)
    image ="""
     /\_)o<
    |      \\
    | O . O|
     \_____/
    """
    print(image)
    print('恭喜'+a+'中奖！')
    return
hellokitty()



num2 = list(range(1,6))
num2.extend('ABCDE')
list2 = [m+n for m in['天字','地字'] fpr n in '一二']
list3 = [n*m for n in range(1,11) if n % 3 == 0]

def card():
    import random
    suit = ['红桃','黑桃','方块','梅花']
    num = list(range(2,11))
    num.extend('JQKA')
    a = random.choice(suit)
    if a == '红桃':
        return 'love you'
    else:
        return 'no'

print(card())









# homework 5-2
students = ['小明', '小红', '小刚']
for i in range(3):
    student1 = students[0]
    students.append(student1)
    del students[0]
    print(students)

students = ['小明', '小红', '小刚']
for i in range(3):
    students1 = students.pop(0)
    students.append(students1)
    print(students)

j = 0
students = ['小明', '小红', '小刚']
while j < 3:
    student2 = students.pop(0)
    students.append(student2)
    print(students)
    j = j + 1

# study 6:
while False:
    print('while False')

print(3 < 5)
print(3 > 5)
print('长安' == '长安')
print('长安' != '金陵')

while 3 > 5:
    print('while False')

if False:
    print('if False')
if True:
    print('if True')

password = input('请输入密码：')

if password == 'abc':
    print('密码正确！')
else:
    print('密码错误！')
if 1:
    print('熊猫')
if '开心':
    print('熊猫')
if '':
    print('熊猫')

print('以下数据判断结果都是【假】：')
print(bool(False))
print(bool(0))
print(bool(''))
print(bool(None))

a = 1
b = -1
print('以下是and运算')
if a==1 and b==1:    # 【b实际上是-1】
    print('True')
else:
    print('False')
print('以下是or运算')
if a==1 or b==1:  # 【b实际上是-1】
    print('True')
else:
    print('False')

# 直接运行代码即可
list = [1,2,3,4,5]
a = 1
# 做一次布尔运算，判断“a是否在列表list之中”
print(bool(a in list))
print(bool(a not in list))

#运行结果会是什么你应该很清楚啦，看看就好~
dict = {'法国':'巴黎','日本':'东京','中国':'北京'}
a = '法国'
print(bool(a in dict))

print(3==3.0)
print('a'!='a')

i = 100
while i:
    print('把这句话打印100遍')
    i = i-

for i in range(5):
    print('明日复明日')
    if i==3:  # 当i等于3的时候触发
        break # 结束循环
i = 0
while i < 5:
    print('明日复明日')
    i = i + 1
    if i == 3:
        break
# 当i等于3的时候触发
    # 结束循环
 i = 0
while i < 5:
    i = i +1
    print('明日复明日')
    if i == 3:
        break
while True:
    print('上供一对童男童女')
    t = input('孙悟空来了吗')
    if t == '来了':
        break
print('孙悟空制服了鲤鱼精，陈家庄再也不用上供童男童女了')

while True:
    t = input('请输入密码：')
    if t == '小龙女':
        break
for i in range(5):
    print('明日复明日')
    if i==3:  # 当i等于3的时候触发
        continue # 回到循环开头
    print('这句话在i等于3的时候打印不出来')
i = 0
while i<5:
    print('明日复明日')
    i = i+1
    if i==3:  # 当i等于3的时候触发
        continue # 回到循环开头
    print('这句话在i等于3的时候打印不出来')
while True:
    q1 = input('第一问：你一生之中，在什么地方最是快乐逍遥？')
    if q1 != '黑暗的冰窖':
        continue
    print('答对了，下面是第二问：')
    q2 = input('你生平最爱之人，叫什么名字？')
    if q2 != '梦姑':
        continue
    print('答对了，下面是第三问：')
    q3 = input('你最爱的这个人相貌如何？')
    if q3 == '不知道':
        break
print('都答对了，你是虚竹。')

for i in range(5):
    a = int(input('请输入0来结束循环，你有5次机会:'))
    if a == 0:
        print('你触发了break语句，循环结束，导致else语句不会生效。')
        break
else:
    print('5次循环你都错过了，else语句生效了。')

n =5
i = 5
while i:
    a = int(input('请输入0结束循环，你有'+str(int(i))+'次机会'))
    n = n -1
    i = i -1
    if a == 0:
        print('你触发了break语句，导致else语句不会生效。')
        break
else:
    print('5次循环你都错过了，else语句生效了')
m = 0
while m <3:
    a = int(input('猜猜看：'))
    if a < 520:
        print('太小了')
        m = m+1
        print('你还剩'+str(int(3-m))+'次机会')
        continue
    if a > 520 :
        print('太大了')
        m = m+1
        print('你还剩' + str(int(3-m)) + '次机会')
        continue
    if  a == 520 :
        print('太好啦，答对了，I LOVE YOU!')
        break
else:
    print('失败了')

 mm = 1314
for i in range(3):
    a = int(input('猜猜看号码'))
    if a == mm:
        print('I LOVE YOU 1314~')
        break
    if a < mm:
        print('太小了')
    elif a > mm:
        print('太大了')
else:
        print('失败了')

#homework:
#exercise:

people = ['青年组','老年组','中年组']
for i in range(3):
    n = input('什么组：')
    if n == people[0]:
        crime1 = input('1认罪吗？')
        crime2 = input('2认罪吗？')
        if crime1 == 'yes' and crime2 == 'yes':
            print('各判决10年')
        elif crime1 == 'no' and crime2 =='no':
            print('各判刑3年')
            break
        else:
            print('认罪的判1年，抵赖的判20年')
    elif n == people[1]:
        crime1 = input('1认罪吗？')
        crime2 = input('2认罪吗？')
        if crime1 == 'yes' and crime2 == 'yes':
            print('各判决10年')
        elif crime1 == 'no' and crime2 == 'no':
            print('各判刑3年')
            break
        else:
            print('认罪的判1年，抵赖的判20年')
    else:
        crime1 = input('1认罪吗？')
        crime2 = input('2认罪吗？')
        if crime1 == 'yes' and crime2 == 'yes':
            print('各判决10年')
        elif crime1 == 'no' and crime2 == 'no':
            print('各判刑3年')
            break
        else:
            print('认罪的判1年，抵赖的判20年')

n = 0
list_answer = []
while True:
    n +=1
    a = input('A，你认罪吗？请回答认罪或者不认：')
    b = input('B，你认罪吗？请回答认罪或者不认：')
    list_answer.append([a,b])
    if a == '认罪' and b == '认罪':
        print('两人都得判10年，唉')
    elif a == '不认' and b == '不认':
        print('都判3年，太棒了')
        break
    else:
        print('认罪的判1年，不认的判20年')
print('第'+str(n)+'对实验选择了最优解')

for i in range(n):
    # 注意数据类型的转换，以及计数起点的不同（0和1）
    print('第' + str(i+1) + '对实验者的选择是：' + str(list_answer[i]))
​


















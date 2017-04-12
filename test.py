# 以#号代表注释
#print('学习python')
#age = int(input('请输入你的年龄:'))
age = 15
if age>=18:
    print('age=',age)
elif age>=12:
    print('hello %d years-old child'%age)
else :
    print('WTF')
print(list(range(21)))

d={'c':11,'b':31}#定义一个dict对象
print('a' in d)#True
print(d.get('a',12),d['c'])#使用get来获取一个key的value,不存在也不会报错，会输出传入的值
#定义一个函数 def 用缩进实现逻辑
def abss(x):
    if x>=0:
        return x
    else :
        return -x
print(abss(-6))
#导入包，调用函数
import math
print(math.pi)
#输出0-99之间的奇数，代码越少越好
L=[]
n=1
for n in range (1,99,2):
    L.append(n)
#第三个参数，隔多少个分割一次
print(L[::20])
#生成器输出斐波那契
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
for i in fib(4):
    print(i)
#输出杨辉三角,强
def triangles():
    g = [1]
    while True:
        yield g
        g.append(0)
        g = [g[i] + g[i-1] for i in range(len(g))]
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
#吧list括起来就成了Iterator
print((x for x in range(10)))
print({'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}['6'])
#用PIL来读取图片，生成缩略图
from PIL import Image
im = Image.open('test.jpg')
print(im.format, im.size, im.mode)
im.thumbnail((200, 100))
im.save('thumb.jpg', 'JPEG')
#class
class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def print_score(self):
        return('{}:{}'.format(self.name,self.score))
    def get_grade(self):
        if self.score >=90:
            return 'A'
        elif self.score >=60:
            return 'B'
        else:
            return 'C'
bart=Student('Bart Simpson',59)
print(bart.print_score(), bart.get_grade())
#父类只输入两个参数(含self)，且父类创建的方法需要该一个参数运行输出，而子类输入三个参数，那此时子类能调用父类的方法吗？

# -*- coding: utf-8 -*-

class Father(object):
    def __init__(self,name):
        self.name=name
    def run1(self):
        print('i am your %s'%self.name)


class Son(Father):
    def __init__(self,mingzi,age):
        Father.__init__(self,mingzi)
        #1、由于要调用的父类方法需要实例变量属性，所以子类也需要绑定实例变量属性
        #2、实例变量属性绑定我目前查到的有3种方式:一是从父类继承，二是从其他类调用，三是自己重新编写绑定
        #3、此处注意输入的是'mingzi'，而不是Father类的name。它实际的属性编写应该对应的是：self.name=mingzi
        #4、不能使用super().__init__(mingzi)，因为如果这里从父类取得属性，那么下面的Uncle类由于不是子类，就无法从Son类取得对应的属性。
        #5、注意引入其他类型属性的编码格式与从父类取得属性两者之间差异，比方说引入其他的：源类型不需加括号，初始化后跟括号里要填写self。
        self.nianling=age#引入其他类型属性格式外，还可以自行编辑想要绑定的属性
    def run2(self):
        print('i am %s,%d years old'%(self.name,self.nianling))

class Uncle(object):
    def __init__(self,name,age):
        Son.__init__(self,name,age)
    def run1(self):
        print('i am your %s,i am %d years old(run1)'%(self.name,self.nianling))
    def run2(self):
        print('i am your %s,i am %d years old(run2)'%(self.name,self.nianling))

def f1(x):#提供一个接口
    x.run1()
    x.run2()

son=Son('Shane',24)
uncle=Uncle('Shane',19)
f1(son)#体现多样性，一个接口，多种实现(父类与子类)
f1(uncle)#体现Python是鸭子类型(不是继承关系)
uncle.run1()
Uncle('lzc',24).run1()



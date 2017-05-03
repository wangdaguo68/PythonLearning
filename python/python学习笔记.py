#List
L = ['Apple', 123, True]
L.append("king")
L.insert(1,"wangdg")
L.pop(2)
print(L)
#Tuple
T=(1,2,3,["wang","da","guo"])
print(T[3][0])

#condition
'''
age=input('please enter your age:')
if int(age)>10:
	print('已成年')
else:
	print('未成年')
'''
#for in
for x in L:
	print(x)
for y in T:
	print(y)
for x,y in [(1, 1), (2, 4), (3, 9)]:			
	print(x,y)
#dict
dict={"a":123,"b":456,"c":789}
print(dict['a'])
print(dict.get('b'))
dict.pop('c')
print(dict)
for x in dict:#x为键，迭代键
	print(x)
for value in dict.values():#value为键对应的值，迭代值
    print(value)	
for k,v in dict.items():#k为键，v为值，迭代键值対
	print(k+str(v))    
#set	
S=set([1,22,3])
S.add(4)
print(S)
S.remove(4)
print(S)
#不可变对象
obj=[2,33,4]
obj.sort()
print(obj)	

#函数定义，调用
def myFunction(num):
	if num>=18:
		return"已成年"
	else:
		return"未成年"
print(myFunction(17))

#引用库
import math
print(round(math.sqrt(2),4))	

#切片
print(L[:5])
print(L[1:3])
print(L[-4:-1])	 	
print(L[-4:])
print(L[:])				

#列表生成式
list=[m + n for m in 'ABC' for n in 'XYZ']
print(list)

#生成器
g = (x * x for x in range(10))
print(g)
print(next(g))

#map高阶函数
def fx(x):
	return x*x
R=map(fx,[1, 2, 3, 4, 5, 6, 7, 8, 9])	
print(R)

#reduce高阶函数
from functools import reduce
def add(x,y):
	return x+y
print(reduce(add,[1,3,5,7,9]))	 

#filter高阶函数
def is_odd(n):
    return n % 2 == 1
print(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))   

#sorted高阶函数
print(sorted([1,4,2,11,6])) 

#lambda表达式
f=lambda x,y:x+y
print(f(1,2))

#装饰器decorator
def deco(func):
    def _deco(a, b):
        print("before myfunc() called.")
        ret = func(a, b)
        print("  after myfunc() called. result: %s" % ret)
        return ret
    return _deco
 
@deco
def myfunc(a, b):
    print(" myfunc(%s,%s) called." % (a, b))
    return a + b

print(myfunc(1,2))    

# -*- coding:gbk -*-
''' 对参数数量不确定的函数进行装饰，
参数用(*args, **kwargs)，自动适应变参和命名参数'''
 
def decoc(func):
    def _decoc(*args, **kwargs):
        print("before %s called." % func.__name__)
        ret = func(*args, **kwargs)
        print("  after %s called. result: %s" % (func.__name__, ret))
        return ret
    return _decoc
@decoc
def myfunction1(a, b):
    print(" myfunction1(%s,%s) called." % (a, b))
    return a + b 
@decoc
def myfunction2(a, b,c):
    print(" myfunction2(%s,%s,%s) called." % (a, b,c))
    return a + b+c     
print(myfunction1(1,2))
print(myfunction2(1,2,3))     

#偏函数  
import functools
int2=functools.partial(int,base=2)
print(int2('1000000'))

#模块
import module
print(module.greeting('wangdg'))
from PIL import Image
im=Image.open('E:\壁纸\sex1.jpeg')
print(im.format, im.size, im.mode)
im.thumbnail((200, 100))
im.save('thumb.png', 'png')


#面向对象
class Person(object):#这里object只的是继承的类，如果没有继承默认写object
	__slots__ = ('name', 'age') #约束class只能定义的属性，这样实例就能动态添加属性
	"""docstring for Person"""
	def __init__(self, name,age):
		super(Person, self).__init__()
		self.name = name
		self.age=age
'''
	def get_Age(self):
        if self.age >= 18:
            return '已成年'
        else:
        	return '未成年'
'''
person=Person('King',26)
print(person.name,person.age)#类属性
#print(person.get_Age())		
print(dir(person))
print(person.__hash__())
#person.property1='test'#实例属性，可以附加，类似js属性
#print(person.property1)

class Student(object):
    @property#装饰器就是负责把一个方法变成属性调用的
    def score(self):
        return self._score

    @score.setter#负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
s=Student()
s.score=80
print(s.score)        

from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
print(dir(Month))    

#IO操作 r w rb wb 读 写 读二进制 写二进制
f=open('D:/开发测试/python/test.txt','w', encoding='utf-8')
f.write('123123')
f.close()
r=open('D:/开发测试/python/test.txt','r', encoding='utf-8')
content=r.read()
print(content)

import os
#print(os.name,os.environ)
print(os.path.abspath('.'))
#os.mkdir('testDic')#创建目录
##os.rmdir('testDic')#删除目录
#os.rename('test.txt', 'test.py')#对文件重命名
#os.remove('test.txt')#删除文件
print([x for x in os.listdir('.') if os.path.isdir(x)])
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])


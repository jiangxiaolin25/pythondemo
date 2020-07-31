#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2019/10/25 11:43
# @Author  : jiangxiaolin
# @Email   : jiangxiaolin@xgd.com
# @File    : stringdemo.py
# @Software: PyCharm

for i in range(-10, 10) :
    print i


def hello() :
   print("Hello World!")

a='测试变量'

class people:
    #定义基本属性
    name = ''
    __name1 = '123'
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法

    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w



    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))

p=people('1',2,75)

print p._people__weight
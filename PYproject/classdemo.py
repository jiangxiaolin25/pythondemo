#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/7/10 10:56
# @Author  : jiangxiaolin
# @Email   : jiangxiaolin@xgd.com
# @File    : classdemo.py
# @Software: PyCharm

class Parent:
    #定义基本属性
    a = '类里面测试变量'
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法

    def __init__(self):
        print "父类的构造函数"
        pass

    def speak(self):
        print("%s 说: 我 %d 岁。" %('张三',5))

    parentAttr = 100
    def parentMethod(self):
        print '调用父类方法'

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print "父类属性 :", Parent.parentAttr


class Child(Parent):  # 定义子类
    __pri="789"
    pul=123
    def __init__(self):
        print "调用子类构造方法"+self.__pri

    def childMethod(self):
        print '调用子类方法'

    def parentMethod(self):
        print '子类方法'

if __name__ == '__main__':
    c=Child()
    c.childMethod()
    c.parentMethod()
    c.setAttr(456)
    print c.getAttr()
    # print c.__pri
    print c.pul
    print c._Child___pri



#!/usr/bin/python3
# _*_ coding:utf-8 _*_
__author__ = 'JXL'
from filetool import *
from classdemo import people
import stringdemo



import time
exitFlag = 0
def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

t="E:/123.txt"
s="F:/b.txt"

def hello(s) :
   print("Hello World!"+s)
   return s+'nihao'

class abcd():



    def copyfiles(self, sou, tar):
        """
        复制一个文件的内容到另一个文件里面
        :param sou: 源文件
        :param tar: 目标文件
        """
        shutil.copyfile(sou, tar)

    def __init__(self,s,t):
        self






if __name__ == '__main__':
    # print_time("1", 1, 5)
    # abcd().copyfiles(t,s)
    # abcd().readfile(t);
    # abcd().hello();
    # c=abcd.aver_age(4,5)
    # abcd.aver_age(4,5)
    # print (c)
    # abcd().copyfiles(t,s)
    # abcd().readlinefile(t)
    # l = ['hello dear!', '\nhello son!', '\nhello baby!']
    # abcd().writenewfile(s,l)
    a='123'
    b='456'
    print ("%s is %s whose age is " %(a,b))
    basket = {'apple', 'orange', 'apple'}# _*_ coding:utf-8 _*_

    for i in range(-10, -100, -30):
         print (i)
    count= 0
    while count < 5:
       print (count, " 小于 5")
       count = count + 1
    else:
       print (count, " 大于或等于 5")

    ticks = time.time()
    print "当前时间戳为:", ticks

    localtime = time.asctime(time.localtime(time.time()))
    print "本地时间为 :", localtime

    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # str = input("请输入：")
    # print "你输入的内容是: ", str
    tup1 = ('physics', 'chemistry', 1997, 2000)
    a="abc"
    print (a.upper())
    print (tup1.count(1997))
    print (tup1.index(1997))
    names = ['mike', 'mark', 'candice', 'laular']
    names2 = ['mike', 'mark', 'candice', 'laular']
    names.append(2)
    print names
    names.insert(0,5)
    print names
    names.reverse()
    print names
    print  names.count(5)
    names.extend(names2)
    print names
    print names.pop(2)
    names.sort( reverse=True)
    print (names)
    zidia={'a':1,'b':2,'j':3}
    print zidia.get('a')
    # 修改字典
    zidia['a']=4
    print zidia
    del zidia['a']
    print zidia
    # filedemo=abcd();
    # filedemo.copyfiles(t,s)
    # people.speak()
    p=people()
    p.speak()
    stringdemo.hello()
    # print p.a
    # print stringdemo.a
    f=filetools()
    # f.readfile(t)
    # f.writeladdfile(t,'\n12456\n789987')
    # f.readfile(t)
    f.speak(t)
    f.readfile(t)




















a=5
b=1
# while a:
#     if b:
#          print "进入b=1里面 %d" %(b)
#     print ("混+%d"%(a))
#     a-=1









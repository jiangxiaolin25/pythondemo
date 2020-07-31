#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2019/10/10 10:39
# @Author  : jiangxiaolin
# @Email   : jiangxiaolin@xgd.com
# @File    : threaddemo.py
# @Software: PyCharm

import threading
import time


class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        for i in range(5) :
         # print ("线程名字："+str(i) + self.name)
         # print ("线程counter：" +str(i)+ self.counter)
         print "第 %s 次 ...线程名字 ： %s 线程ID是 %d counter 值是 %d" %(str(i),self.name,self.threadID,self.counter)
         # print ("线程ID：" +str(i)+ self.threadID)
         time.sleep(1)
         self.counter-=1
         # print ("退出线程：" + self.name)
if __name__ == '__main__':
    th1=myThread(1,"th-1",5)
    th2=myThread(2,"th-2",5)
    # th1.start()
    # th1.join()
    # th2.start()
    print time.ctime(time.time())














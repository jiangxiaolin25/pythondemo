#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 19:35
# @Author  : jiangxiaolin
# @Email   : jiangxiaolin@xgd.com
# @File    : pyPKjava.py
# @Software: PyCharm
import time

ticks = time.time()
print "当前时间戳为:", ticks

for i in range(0,9999999):
    print i

print time.time()-ticks
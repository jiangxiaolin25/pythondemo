#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/7/10 17:04
# @Author  : jiangxiaolin
# @Email   : jiangxiaolin@xgd.com
# @File    : matchdemo.py
# @Software: PyCharm
import re

# s="123aabcABC78a9AAAA"
# a=re.match('.+a',s)
# print a.group()
# # print"*:"+(re.match('w*', 'wwwwwwwwwwww.runoob.wwwwcom').group())
# # print"+:"+(re.match('w+', 'wwwwwwwwwwww.runoob.wwwwcom').group())
# print"*:"+(re.search('w*', '1wwwwwwwwwwww.runoob.wwwwcom').group())
# print"+:"+(re.search('w+', '111111wwwwwwwwwwww.runoob.wwwwcom').group())
# print"^:"+(re.match('^[0-9]', '8www.runoob.wwwwcom').group())
# print"^:"+(re.match('^[089]', '9www.runoob.wwwwcom').group())
# # print"$:"+(re.match('[a-z]$', 'www.runoob.wwwwcom').group())
# print"$:"+(re.search('[a-z]$', 'www.runoob.wwwwcom').group())
# s = "g23 abc8"
#
#
# print re.findall('^[0-9]',s)
# print re.findall('[0-9]$',s)
#
# print(re.findall('o*', 'www.runoob.wwwwcom'))
# print(re.findall('o*', 'www.runoob.wwwwcom'))
# print 'findall'+(re.findall('^w', 'www.runoob.wwwwcom'))
# print(re.findall('o*', 'www.runoob.wwwwcom'))
'''
\b 匹配单词的开始或者结束
     	匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'
[^a]匹配出了a以外的任意字符
? 重复0次或者1次
{n}重复n次
{n,m}重复n-m次
serarch:只匹配第一个，匹配到了就暂停了
findall:匹配所有
match：开头不匹配就立即暂停匹配



'''

s0="www.ASD456789dcb.com"
s1="ASD356456789com"
s2="ASDcom"
re_compile = re.compile("ASD[0-9]*com")
re_compile1 = re.compile("ASD{3,5}com")
print re.findall(re_compile,s1)
print re.findall(re_compile,s2)
print re.findall(re_compile1,s1)










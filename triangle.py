#!/usr/bin/env python
#coding=utf-8
#title        : triangle.py
#description  : 打印杨辉三角
#author       : Hamlet_Jiaxiaoyu
#email        : zhengdf936@163.com
#date         : 2018-1-11
#notes        :

def triangles():
    b = [1]
    while True:
        yield b
        b = [1] + [b[i] + b[i+1] for i in range(len(b)-1)] + [1]
        
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break

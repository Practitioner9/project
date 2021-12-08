#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :send_gift.py
# @Time      :2021/12/6 0006 下午 8:47
# @Author    :幸运
# @Software  :PyCharm

#from project.gift import have_gift
import gift
#发送礼物
def send_gift():
    #发礼物
    #声明要做全局变量
    #global have_gift
    #局部变量
    gift.have_gift = True
    #获取当前礼物发放的状态
    gift_stutas = gift.have_gift
    #打印当前礼物的状态
    print(f"当前的礼物状态为：{gift_stutas}")
    #打印have_gift的内存地址
    #print("gift_stutas id",id(have_gift))
    print("发礼物啦~~ ")
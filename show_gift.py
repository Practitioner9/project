#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :show_gift.py
# @Time      :2021/12/6 0006 下午 8:47
# @Author    :幸运
# @Software  :PyCharm
#from project.gift import have_gift
import gift
#显示礼物
def show_dift():
    if gift.have_gift == True:
        print("收到礼物啦，很开心~~")
    else:
        print("没有收到礼物，等待中~~")
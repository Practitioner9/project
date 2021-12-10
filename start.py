#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :start.py
# @Time      :2021/12/6 0006 下午 8:48
# @Author    :幸运
# @Software  :PyCharm

#入口函数
from project.gift import have_gift
from project.send_gift import send_gift
from project.show_gift import show_dift
if __name__ == '__main__':
    #调用函数
    send_gift()
    show_dift()

    #print(have_gift)
    #print("全局变量为 id ",id(have_gift))
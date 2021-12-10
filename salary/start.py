#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :start.py
# @Time      :2021/12/8 0008 下午 10:19
# @Author    :幸运
# @Software  :PyCharm

from project.salary.select_money import select_money
from project.salary.send_money import send_money

if __name__ == '__main__':
    #调用函数

    send_money(1000)
    select_money()
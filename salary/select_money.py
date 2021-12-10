#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :select_money.py
# @Time      :2021/12/8 0008 下午 10:18
# @Author    :幸运
# @Software  :PyCharm
import project.salary.money as m
import project.salary.send_money as s


def select_money():

    current_money= m.saved_money + s.send_money1
    print(f"工资发到手里啦：{current_money}")

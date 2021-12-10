#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :send_money.py
# @Time      :2021/12/8 0008 下午 10:18
# @Author    :幸运
# @Software  :PyCharm

# 定义发工资模块 send_money.py，用来增加收入计算

send_money1 = 0


def send_money(salary):
    if salary == 1000:
        global send_money1
        send_money1 = salary
        print(f"发工资了:{salary}")
    else:
        print("等待发工资中~~")

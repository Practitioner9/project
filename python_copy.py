#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :python_copy.py
# @Time      :2021/12/6 0006 下午 9:00
# @Author    :幸运
# @Software  :PyCharm
import copy
a = [1,2,3,['a','b']]
#赋值
b = a
#浅拷贝
c = copy.copy(a)

#深拷贝
d = copy.deepcopy(a)

#修改a
a.append(4)
#修改a 中的子对象
a[3].append('c')
#打印查看修改之后的变量的值
print("a= ",a)
print("b= ",b)
print("c= ",c)
print("d= ",d)
#打印出来的结果
a=  [1, 2, 3, ['a', 'b', 'c'], 4]
b=  [1, 2, 3, ['a', 'b', 'c'], 4]
c=  [1, 2, 3, ['a', 'b', 'c']]
d=  [1, 2, 3, ['a', 'b']]

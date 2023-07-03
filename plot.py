#!/usr/bin/env python
# coding: utf-8

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# 必须配置中文字体，否则会显示成方块
# 注意所有希望图表显示的中文必须为unicode格式
#custom_font = mpl.font_manager.FontProperties(fname='/Library/Fonts/华文细黑.ttf')

font_size = 10 # 字体大小
fig_size = (8, 6) # 图表大小

names = (u'energy', u'charge') # 姓名
subjects = ('-0.25', '-0.2', '-0.15', '-0.1', '-0.05', '0.001', '0.05', '0.1', '0.15', '0.2', '0.25') # 科目
scores = ((0.12937, 0.12325, 0.11913, 0.11511, 0.11339, 0.11224, 0.11293, 0.11515, 0.11866, 0.12372, 0.13037), (3.25926, 3.23543,3.18767,3.16147,3.13476,3.12229,3.09435, 3.04868, 3.01252, 2.90142, 2.88589)) # 成绩

x= np.arange(10)
y1 = x**2
y2 = x**4
_,ax=plt.subplots()

ax.plot(subjects,scores[1],'r')
ax.set_xlabel('x')
ax.set_ylabel('y1',color='b')
ax2 = ax.twinx()
ax2.plot(subjects,scores[1],'r')
ax2.set_ylabel('y2',color='r')

# 图表输出到本地
plt.savefig('scores_par.png')
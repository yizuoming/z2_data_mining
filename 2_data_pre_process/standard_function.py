# -*- coding: utf-8 -*-
"""
数据规范处理

为什么要做数据规范(归一化处理):

是为了减少数据在可视化是的距离差异：
（如：将数据 X1薪水：4023、5000、8000 X2年龄：40、33、30，将这些数据按照一定的比例尽量处理到-1跟1之间）
"""
import base as B

input_file='../0_data_file/pre/normalization_data.xls'
#无表头
data=B.in_excel_header(input_file,"")
# 最小-最大规范化
print((data - data.min())/(data.max() - data.min()))
# 零-均值规范化
print((data - data.mean())/data.std())
# 小数定标规范化
print(data/10**B.np.ceil(B.np.log10(data.abs().max())))


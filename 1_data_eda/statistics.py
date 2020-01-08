# -*- coding: utf-8 -*-
"""
统计相关
"""
import base as B

input_file='../0_data_file/eda/catering_sale.xls'
df=B.in_excel(input_file,u'日期')
df = df[(df["销量"] > 400) & (df["销量"] < 5000)]
print("数据基本信息:{0}".format(df.describe()))
db=df.describe()
# 极差
db.loc['range']=db.loc['max'] - db.loc['min']
#变异系数
#在概率论和统计学中，变异系数，又称“离散系数”（英文：coefficient of variation），是概率分布离散程度的一个归一化量度，其定义为标准差与平均值之比
db.loc['var']=db.loc['std'] / db.loc['mean']
# 四分位数间距
#是描述统计学中的一种方法，以确定第三四分位数和第一四分位数的分别（即 的差距）。与方差、标准差一样，表示统计资料中各变量分散情形，但四分差更多为一种稳健统计
db.loc['dis']=db.loc['75%']-db.loc['25%']
print("统计后的基本信息:{0}".format(db))


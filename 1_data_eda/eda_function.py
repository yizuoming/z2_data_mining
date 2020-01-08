# -*- coding: utf-8 -*-
"""
数据探索常用方法
"""
import base as B

input_file='../0_data_file/eda/test.xlsx'
data=B.pd.read_excel(input_file,index_col='ID')
print("基本统计量")
print(data.describe())
print(type(data.describe()))
print(data.describe().loc["mean"])
print("数据类型",type(data))
print("打印某列",data['A'])
print("整体求和",data.sum())
print("某列求和",data['A'].sum())
print("avg",data.mean())
print("方差",data.var())
print("标准差",data.std())
print("相关系数1",data.corr(method='pearson'))
print("相关系数2",data['A'].corr(data['B']))
#协方差表示两个变量的总体误差
print("协方差矩阵",data.cov())
print(data.loc[101].cov(data.loc[102]))
print("阶距",data.skew())

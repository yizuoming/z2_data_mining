# -*- coding: utf-8 -*-
"""
异常值分析
箱线图也称箱须图、箱形图、盒图，用于反映一组或多组连续型定量数据分布的中心位置和散布范围。
箱形图包含数学统计量，不仅能够分析不同类别数据各层次水平差异，还能揭示数据间离散程度、异常值、分布差异等等

在箱线图中，箱子的中间有一条线，代表了数据的中位数。箱子的上下底，分别是数据的上四分位数（Q3）和下四分位数（Q1），
这意味着箱体包含了50%的数据。因此，箱子的高度在一定程度上反映了数据的波动程度。上下边缘则代表了该组数据的最大值和最小值。有时候箱子外部会有一些点，可以理解为数据中的“异常值”

https://www.sohu.com/a/218322591_416207

"""
import base as B


input_file='../0_data_file/eda/catering_sale.xls'
df=B.in_excel(input_file,u'日期')
print("数据量:",len(df))
print("数据基本信息:",df.describe())

#箱型图
B.plt.figure()
p=df.boxplot(return_type='dict')
#异常数据
x=p['fliers'][0].get_xdata()
y=p['fliers'][0].get_ydata()
y.sort()

for i in range(len(x)):
    if i > 0:
        # xy为注释坐标点，xytext为注释文字的位置
        B.plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i]+0.05-0.8/(y[i]-y[i-1]), y[i]))
    else:
        B.plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i]+0.08, y[i]))
B.plt.show()







